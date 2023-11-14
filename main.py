import requests
import smtplib
from datetime import datetime


MY_LAT = 49.052502 # Your latitude
MY_LONG = 2.038830 # Your longitude

my_mail = "bdiop8683@gmail.com"
password = "awfwyapbrggeaglv "

def near_latitude(latitude):
    return ((latitude-5)<MY_LAT or (latitude+5)>=MY_LAT)


def near_longitude(longitude):
    return ((longitude- 5) < MY_LONG or (longitude + 5) >= MY_LONG)


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

def is_dark(hour):
    return sunset<= hour <= sunrise

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if near_latitude(iss_latitude) and near_longitude( iss_longitude) and is_dark(time_now.hour):
    with smtplib.SMTP("smtp.gmail.com") as connection :
        connection.starttls()
        connection.login(user= my_mail, password=password)
        connection.sendmail(from_addr=my_mail,to_addrs="baba78122@gmail", msg="ISS is near, look up")
else:
    print("ISS is far")


print(f"Subject:ISS is here\n\nISS longitude : {iss_longitude}, ISS latitude : {iss_latitude}")
