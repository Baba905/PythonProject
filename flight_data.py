from flight_search import FlightSearch

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,price, departure_city,departure_airport,arrival_city,arrival_airport,outbound_date,inbound_date):
        self.price = price
        self.departure_city = departure_city
        self.departure_airport = departure_airport
        self.arrival_city = arrival_city
        self.arrival_airport = arrival_airport
        self.outbound_date = outbound_date
        self.inbound_date = inbound_date


text = f"Low price alert! Only {1}€ to fly from {2}" \
       f"from you {2}"