import smtplib
import datetime as dt
import random


# Constants
MY_EMAIL = "test@gmail.com"
TO_EMAIL = "test1@gmail.com"
PASSWORD = "test"
PORT = 587

# Get current date and time
current_date_time = dt.datetime.now()
current_day = current_date_time.weekday()

# Send email if it's Monday
if current_day == 0:
    with open("quotes.txt", mode="r") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", PORT) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
else:
    print("It's not Monday")