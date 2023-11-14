import  requests
from twilio.rest import Client

api_key = "98ba4112dea4f5b2d323c6f48689ac69"
parameters = {
    "appid": api_key,
    "lat": "47.376888",
    "lon": "8.541694",
    "units": "metric",
    "exclude": "current,daily,minutely",
}

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall",params= parameters)
print(response.url)
response.raise_for_status()
data = response.json()
twelve_hours = data["hourly"][:12]
weather_id_hour = [elt["weather"][0]["id"] for elt in twelve_hours]

will_rain = False
print(weather_id_hour)
for id in weather_id_hour:
    if id < 700 :
        will_rain = True


if will_rain:
    account_sid = 'AC6ce10be0a341dd7d155ecfdd4a168aad'
    auth_token = '220d009b964e1d38147d7c4413bb8125'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
      from_='+15074018389',
      to='+33672341635',
      body= "Hello Baba! It's go to rain today don't forget your umbrella.☂️"

    )
    print(message.status)