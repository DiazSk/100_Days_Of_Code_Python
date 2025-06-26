##################### Extra Hard Starting Project ######################
import pandas as pd
import random
import smtplib
import datetime as dt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Constants
MY_EMAIL = "test@gmail.com"
PASSWORD = "test"
PORT = 587

# Read birthdays.csv
birthdays_df = pd.read_csv("birthdays.csv")

# Get today's date
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# Find birthdays today
birthday_today = birthdays_df[(birthdays_df["month"] == today_tuple[0]) & (birthdays_df["day"] == today_tuple[1])]

if not birthday_today.empty:
    for index, row in birthday_today.iterrows():
        name = row["name"]
        email = row["email"]
        letter_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(letter_path, encoding='utf-8') as letter_file:
            letter_content = letter_file.read()
            letter_content = letter_content.replace("[NAME]", name)

        # Create properly formatted email message with UTF-8 encoding
        msg = MIMEMultipart()
        msg['From'] = MY_EMAIL
        msg['To'] = email
        msg['Subject'] = "Happy Birthday!"
        
        # Attach the letter content as UTF-8 text
        msg.attach(MIMEText(letter_content, 'plain', 'utf-8'))
        
        with smtplib.SMTP("smtp.gmail.com", PORT) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=msg.as_string()
            )

else:
    print("No birthdays today")