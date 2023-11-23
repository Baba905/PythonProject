import requests
from pprint import pprint

DATA_KEY = "Bearer hhfdfkljklvuooie53244fkd"
data_endpoint = "https://api.sheety.co/327fc4c1ddf7fefbbfb7d8f3719fe01d/flightDeals/prices"

data_header ={
    "Authorization": DATA_KEY,
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def get(self):
        response = requests.get(url=data_endpoint, headers=data_header)
        response.raise_for_status()
        return  response.json()


    def put(self, price,id):
        endpoint = f"{data_endpoint}/{id}"
        parameter = {
            "price":{
                'lowestPrice': price,
            }
        }
        reponse = requests.put(url=endpoint, json=parameter, headers=data_header)
        reponse.raise_for_status()



# data = DataManager().get()
# pprint(data)