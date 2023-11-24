import requests
from pprint import pprint

DATA_KEY = "Bearer"
data_flight_endpoint = "https://api.sheety.co/327fc4c1ddf7fefbbfb7d8f3719fe01d/flightDeals/prices"

data_user_endpoint = "https://api.sheety.co/327fc4c1ddf7fefbbfb7d8f3719fe01d/flightDeals/users"
data_header ={
    "Authorization": DATA_KEY,
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def get_flight(self):
        response = requests.get(url=data_flight_endpoint, headers=data_header)
        response.raise_for_status()
        return  response.json()


    def put(self, price,id):
        endpoint = f"{data_flight_endpoint}/{id}"
        parameter = {
            "price":{
                'lowestPrice': price,
            }
        }
        reponse = requests.put(url=endpoint, json=parameter, headers=data_header)
        reponse.raise_for_status()

    def get_user(self):
        response = requests.get(url=data_user_endpoint, headers=data_header)
        response.raise_for_status()
        return response.json()

# data = DataManager().get_user()
# pprint(data)