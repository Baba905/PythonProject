
import pandas as pd
import datetime as dt
import smtplib
import random
import  os

LETTERS = os.listdir("letter_templates")
my_mail = "bdiop8683@gmail.com"
password = "awfwyapbrggeaglv "

def message(name):
    letter_path = "letter_templates/"+random.choice(LETTERS)
    with open(letter_path, 'r') as file:
        text = file.read()
    text = text.replace("[NAME]", name)
    return text

def sent_email(email, name):
    msg = message(name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail, to_addrs=email, msg=f"Subject:Hapy Birthday\n\n {msg}\n")


friends_dataframe = pd.read_csv("birthdays.csv")
friends_dict = {(row.month,row.day): row for (index,row) in friends_dataframe.iterrows()}

today =(dt.datetime.now().month,dt.datetime.now().day)

if today in friends_dict.keys():
    friend = friends_dict.get(today)
    sent_email(friend["email"], friend["name"])

