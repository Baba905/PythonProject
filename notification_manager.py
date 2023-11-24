import requests
from twilio.rest import Client
from flight_data import FlightData
from flight_search import FlightSearch
import smtplib

my_mail = "bdiop8683@gmail.com"
password = "khnggyyukaordocn"
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def message(self, flight_data):
        account_sid = ''
        auth_token = ''
        client = Client(account_sid, auth_token)

        text = f"Low price alert! Only {flight_data.price}€ to fly from {flight_data.departure_city}-{flight_data.departure_airport} to {flight_data.arrival_city}-{flight_data.arrival_airport}, from {flight_data.outbound_date} to {flight_data.inbound_date}."

        if flight_data.stopovers >= 1 :
            text = text+f"\nFlight has 1 stop over, via {flight_data.viacity}"

        message = client.messages.create(
            from_='+15074018389',
            to='Phone Number',
            body= text,

        )
        print(message.status)

    def send_email(self,email,name, flight_data):
        msg = f"Low price alert! Only {flight_data.price}€ to fly from {flight_data.departure_city}-{flight_data.departure_airport} to {flight_data.arrival_city}-{flight_data.arrival_airport}, from {flight_data.outbound_date} to {flight_data.inbound_date}."
        if flight_data.stopovers >= 1 :
            msg = msg+f"\nFlight has 1 stop over, via {flight_data.viacity}."

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_mail, password=password)
            connection.sendmail(from_addr=my_mail, to_addrs=email, msg=f"Subject: Flight Deal{name}\n\n {msg.encode('utf-8')}\n")


# search = FlightSearch().lowest_flight("LON", 1, 1)
# flight_data = FlightData(search[0]["price"], search[0]["departure_city"], search[0]["departure_airport"],
#                                  search[0]["arrival_city"], search[0]["arrival_airport"], search[0]["outbound_date"],
#                                  search[0]["inbound_date"])
# not_m = NotificationManager()
# not_m.send_email("baba78122@gmail.com",flight_data)