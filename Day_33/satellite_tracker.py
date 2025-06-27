import os
import requests
import logging
from datetime import datetime, timezone
from typing import Dict, Tuple, Optional
from dataclasses import dataclass


# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class Location:
    """Represents a geographic location."""
    latitude: float
    longitude: float
    
    def __post_init__(self):
        """Validate coordinates."""
        if not (-90 <= self.latitude <= 90):
            raise ValueError(f"Invalid latitude: {self.latitude}")
        if not (-180 <= self.longitude <= 180):
            raise ValueError(f"Invalid longitude: {self.longitude}")


@dataclass
class ISSPosition:
    """Represents ISS position data."""
    latitude: float
    longitude: float
    timestamp: datetime


@dataclass
class SunTimes:
    """Represents sunrise and sunset times."""
    sunrise_hour: int
    sunset_hour: int


class SpaceAPIClient:
    """Client for space-related APIs."""
    
    def __init__(self, timeout: int = 10):
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'ISS-Tracker/1.0'})
    
    def get_iss_position(self) -> Optional[ISSPosition]:
        """Get current ISS position."""
        url = "http://api.open-notify.org/iss-now.json"
        
        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            data = response.json()
            position_data = data['iss_position']
            
            logger.info("Successfully retrieved ISS position")
            return ISSPosition(
                latitude=float(position_data['latitude']),
                longitude=float(position_data['longitude']),
                timestamp=datetime.fromtimestamp(data['timestamp'], tz=timezone.utc)
            )
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to get ISS position: {e}")
            return None
    
    def get_sun_times(self, location: Location) -> Optional[SunTimes]:
        """Get sunrise and sunset times for a location."""
        url = "http://api.sunrise-sunset.org/json"
        params = {
            "lat": location.latitude,
            "lng": location.longitude,
            "formatted": 0,
        }
        
        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            
            data = response.json()
            if data['status'] != 'OK':
                raise ValueError(f"API returned status: {data['status']}")
            
            results = data['results']
            sunrise = datetime.fromisoformat(results['sunrise'].replace('Z', '+00:00'))
            sunset = datetime.fromisoformat(results['sunset'].replace('Z', '+00:00'))
            
            logger.info("Successfully retrieved sun times")
            return SunTimes(
                sunrise_hour=sunrise.hour,
                sunset_hour=sunset.hour
            )
            
        except (requests.exceptions.RequestException, ValueError, KeyError) as e:
            logger.error(f"Failed to get sun times: {e}")
            return None
    
    def close(self):
        """Close the session."""
        self.session.close()


def get_location_from_env() -> Location:
    """Get location from environment variables with fallback to Seattle."""
    try:
        lat = float(os.getenv('LATITUDE', '47.855019'))
        lng = float(os.getenv('LONGITUDE', '-122.217400'))
        return Location(lat, lng)
    except ValueError as e:
        logger.warning(f"Invalid coordinates in environment: {e}. Using Seattle as fallback.")
        return Location(47.855019, -122.217400)


def satellite_tracker():
    """Main function to demonstrate ISS tracking and sun times."""
    location = get_location_from_env()
    logger.info(f"Using location: {location.latitude}, {location.longitude}")
    
    client = SpaceAPIClient()
    
    try:
        # Get ISS position
        iss_position = client.get_iss_position()
        if iss_position:
            logger.info(f"ISS Position: {iss_position.latitude}, {iss_position.longitude}")
            logger.info(f"Timestamp: {iss_position.timestamp}")
        else:
            logger.warning("Could not retrieve ISS position")
        
        # Get sun times
        sun_times = client.get_sun_times(location)
        if sun_times:
            logger.info(f"Sunrise hour: {sun_times.sunrise_hour}")
            logger.info(f"Sunset hour: {sun_times.sunset_hour}")
        else:
            logger.warning("Could not retrieve sun times")
        
        # Current time
        current_time = datetime.now(timezone.utc)
        logger.info(f"Current UTC hour: {current_time.hour}")
        
    finally:
        client.close()


if __name__ == "__main__":
    satellite_tracker()


