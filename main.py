#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


data = DataManager()
flight_search = FlightSearch()
notification = NotificationManager()

sheet_data= data.get()["prices"]

for  elt in sheet_data:
    search = flight_search.lowest_flight(elt["iataCode"],1,1)
    if search["price"] < elt["lowestPrice"] :
        data.put(search["price"], elt["id"])
        flight_data = FlightData(search["price"],search["departure_city"],search["departure_airport"],search["arrival_city"],search["arrival_airport"],search["outbound_date"],search["inbound_date"])
        notification.message(flight_data)

# pprint(sheet_data)



#pprint(sheet_data)