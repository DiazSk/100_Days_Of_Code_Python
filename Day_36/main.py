import requests
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

NEWS_API_KEY = "28fef2a2c83d4ab7b594c945d2c12853"
NEWS_PRICE_URL = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "YZOU8GBG3W4ZYB6N"
STOCK_PRICE_URL = "https://www.alphavantage.co/query"

FROM_EMAIL = "zaid07sk@gmail.com"
To_EMAIL = "zaid2002sk@gmail.com"
# Use environment variable or App Password instead of regular password
MY_PASSWORD = ""  # You'll need to replace this with an App Password

# Gmail SMTP settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "outputsize": "compact",
    "apikey": STOCK_API_KEY,
}

news_params = {
    "q": "Tesla",
    "apikey": NEWS_API_KEY,
}

def send_email(subject, body):
    """Send email with proper error handling"""
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = FROM_EMAIL
        msg['To'] = To_EMAIL
        msg['Subject'] = subject
        
        # Add body to email
        msg.attach(MIMEText(body, 'plain'))
        
        # Create SMTP session
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable security
            server.login(FROM_EMAIL, MY_PASSWORD)
            text = msg.as_string()
            server.sendmail(FROM_EMAIL, To_EMAIL, text)
        
        print("Email sent successfully!")
        return True
        
    except smtplib.SMTPAuthenticationError:
        print("SMTP Authentication Error: Check your email and password.")
        print("For Gmail, you need to use an App Password instead of your regular password.")
        print("Visit: https://support.google.com/accounts/answer/185833")
        return False
    except smtplib.SMTPException as e:
        print(f"SMTP Error: {e}")
        return False
    except TimeoutError:
        print("Connection timeout. Check your internet connection or try again later.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

try:
    # Get stock data
    print("Fetching stock data...")
    response = requests.get(STOCK_PRICE_URL, params=stock_params)
    response.raise_for_status()
    stock_data = response.json()

    # Get news data
    print("Fetching news data...")
    response = requests.get(NEWS_PRICE_URL, params=news_params)
    response.raise_for_status()
    news_data = response.json()

    # Get the latest available dates (since markets might be closed)
    time_series = stock_data["Time Series (Daily)"]
    dates = list(time_series.keys())
    dates.sort(reverse=True)  # Most recent first
    
    if len(dates) < 2:
        print("Not enough data to compare stock prices")
        exit()
    
    latest_date = dates[0]
    previous_date = dates[1]
    
    latest_price = float(time_series[latest_date]["4. close"])
    previous_price = float(time_series[previous_date]["4. close"])
    
    difference = latest_price - previous_price
    percentage_change = (difference / previous_price) * 100
    
    print(f"Latest price ({latest_date}): ${latest_price:.2f}")
    print(f"Previous price ({previous_date}): ${previous_price:.2f}")
    print(f"Change: ${difference:.2f} ({percentage_change:+.2f}%)")
    
    # Determine if change is significant (you can adjust this threshold)
    threshold = 5.0  # 5% change
    
    if abs(percentage_change) > threshold:
        direction = "📈 UP" if difference > 0 else "📉 DOWN"
        arrow = "🔺" if difference > 0 else "🔻"
        
        subject = f"Tesla Stock Alert - {direction}"
        
        # Get top news articles
        articles = news_data.get("articles", [])[:3]  # Get top 3 articles
        news_section = ""
        if articles:
            news_section = "\n\n--- Related News ---\n"
            for i, article in enumerate(articles, 1):
                news_section += f"{i}. {article['title']}\n"
                news_section += f"   {article['url']}\n\n"
        
        body = f"""Tesla Stock Price Update

{arrow} Tesla stock is {direction.split()[1]} by ${abs(difference):.2f} ({percentage_change:+.2f}%)

Current Price: ${latest_price:.2f}
Previous Price: ${previous_price:.2f}
Change: ${difference:+.2f}

Date: {latest_date}{news_section}"""
        
        print(f"\nSignificant change detected! Sending email...")
        send_email(subject, body)
    else:
        print(f"Change is not significant (less than {threshold}%). No email sent.")

except requests.RequestException as e:
    print(f"Error fetching data: {e}")
except KeyError as e:
    print(f"Error parsing data: {e}")
    print("Check if your API keys are valid and the data structure is correct.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")