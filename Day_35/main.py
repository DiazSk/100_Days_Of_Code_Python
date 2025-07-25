import requests
import smtplib


OPEN_WEATHER_MAP_URL = "https://api.openweathermap.org/data/2.5/forecast"
OPEN_WEATHER_API_KEY = "your_api_key"

MY_EMAIL = "test@test.com"
MY_PASSWORD = "test"


params = {
    "lat": 47.855019,
    "lon": -122.217400,
    "appid": OPEN_WEATHER_API_KEY,
    "cnt": 4,
    "units": "metric",
    "lang": "en",
}


response = requests.get(OPEN_WEATHER_MAP_URL, params=params)
response.raise_for_status()

weather_data = response.json()

# weather_id = weather_data["list"][0]["weather"][0]["id"]

for hour_data in weather_data["list"]:
    if hour_data["weather"][0]["id"] < 700:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:It's going to rain today. Remember to bring an umbrella.\n\nIt's going to rain today. Remember to bring an umbrella.",
            )
    else:
        print("No umbrella needed")









