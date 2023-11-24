#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


data = DataManager()
flight_search = FlightSearch()
notification = NotificationManager()

sheet_data_flight = data.get_flight()["prices"]
sheet_data_user = data.get_user()["users"]

for  elt in sheet_data_flight:
    try :
        search = flight_search.lowest_flight(elt["iataCode"],1,1)
    except IndexError :
        search = flight_search.lowest_flight(elt["iataCode"],1,1,2)
        flight_data = FlightData(search[0]["price"], search[0]["departure_city"], search[0]["departure_airport"],
                                 search[0]["arrival_city"], search[0]["arrival_airport"], search[0]["outbound_date"],
                                 search[0]["inbound_date"],2,search[1]["origin_city"])
        # pprint(search)
    else :
        flight_data = FlightData(search[0]["price"], search[0]["departure_city"], search[0]["departure_airport"],
                                 search[0]["arrival_city"], search[0]["arrival_airport"], search[0]["outbound_date"],
                                 search[0]["inbound_date"])
    # pprint(elt)
    if search[0]["price"] < elt["lowestPrice"] :
        data.put(search[0]["price"], elt["id"])
        notification.message(flight_data)
        for user in sheet_data_user:
            name = user["firstName"]+" "+user["lastName"]
            notification.send_email(user["email"], name, flight_data)
    pprint(elt)