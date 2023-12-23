import requests
from bs4 import BeautifulSoup

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
web_page = response.text
soup = BeautifulSoup(web_page, 'html.parser')

class Scrapping :

    def __init__(self):
        self.list_of_li_tag = soup.select('li.ListItem-c11n-8-84-3-StyledListCardWrapper')
        self.prices = []
        self.address =[]
        self.links =[]

    def set_address(self):
        for li_tag in self.list_of_li_tag:
            tmp = li_tag.select("address")[0].getText().replace("  ", "").split("\n")[1]
            self.address.append(tmp)

    def set_prices(self):
        for li_tag in self.list_of_li_tag:
            tmp = li_tag.select("span[data-test='property-card-price']")[0].getText()
            if '+' in tmp:
                tmp = tmp.split("+")[0]
            elif "/" in tmp:
                tmp = tmp.split("/")[0]
            self.prices.append(tmp)

    def set_links(self):
        self.links= [li_tag.select("a[class='property-card-link']")[0].get("href") for li_tag in self.list_of_li_tag]