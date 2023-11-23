import  requests
from pprint import pprint
import datetime as dt

FlIGHT_SEARCH_KEY = "vJ-VzhFjSxBR0jobIu7tv8Zn0usqZ9uY"
flight_search_location_endpoint = "https://api.tequila.kiwi.com/locations/query"
flight_search_endpoint = 'https://api.tequila.kiwi.com/v2/search'

FlIGHT_SEARCH_HEADER = {
    'apikey': FlIGHT_SEARCH_KEY,
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_iata(self, city_name):
        parameter = {
            "term": city_name,
            "location_types": "city",
        }

        response = requests.get(url=flight_search_location_endpoint, params= parameter, headers=FlIGHT_SEARCH_HEADER)
        response.raise_for_status()
        return response.json()["locations"][0]["code"]

    def lowest_flight(self,destination,nb_hold_bag, nb_hand_bag):
        today = dt.datetime.today()
        date_from = today + dt.timedelta(days=1)
        date_to = today + dt.timedelta(days=120)

        parameters = {
            "fly_from": "PAR",
            "fly_to": destination,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": "7",
            "nights_in_dst_to":  "28",
            "max_fly_duration": "20",
            "adults": "1",
            "selected_cabins": "M",
            "adult_hold_bag": str(nb_hold_bag),
            "adult_hand_bag": str(nb_hand_bag),
            "curr": "EUR",
            "max_stopovers": "0",
            "limit": '1',
        }

        response = requests.get(url= flight_search_endpoint, params= parameters, headers= FlIGHT_SEARCH_HEADER)
        # pprint(response.text)
        response.raise_for_status()
        data = response.json()["data"][0]

        result = {
            "price": data["price"],
            "departure_city": data["cityFrom"],
            "departure_airport": data["flyFrom"],
            "arrival_city": data["cityTo"],
            "arrival_airport": data["flyTo"],
            "outbound_date": data["local_departure"].split('T')[0],
            "inbound_date": data['route'][1]["local_departure"].split('T')[0],
        }


        return result

# test = FlightSearch().lowest_flight("LON", 1,1)
# pprint(test)