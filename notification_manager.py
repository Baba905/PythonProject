import requests
from twilio.rest import Client
from flight_data import FlightData
from flight_search import FlightSearch

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def message(self, flight_data):
        account_sid = 'AC6ce10be0a341dd7d155ecfdd4a168aad'
        auth_token = '080bdcb8dbb56bf3f228db805a0ccf43'
        client = Client(account_sid, auth_token)

        text = f"Low price alert! Only {flight_data.price}€ to fly from {flight_data.departure_city}-{flight_data.departure_airport} to {flight_data.arrival_city}-{flight_data.arrival_airport}, from {flight_data.outbound_date} to {flight_data.inbound_date}"


        message = client.messages.create(
            from_='+15074018389',
            to='+33672341635',
            body= text,

        )
        print(message.status)


# search = FlightSearch().lowest_flight("LON", 1, 1)
# flight_data = FlightData(search["price"],search["departure_city"],search["departure_airport"],search["arrival_city"],search["arrival_airport"],search["outbound_date"],search["inbound_date"])
# print(flight_data)
# not_m = NotificationManager()
# not_m.message(flight_data)