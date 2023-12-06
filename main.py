from pprint import pprint
import smtplib
import requests
from bs4 import BeautifulSoup

my_mail = "bdiop8683@gmail.com"
password ="flqysukomcvkavdz "
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Accept-Language": "en-US,en;q=0.5",
}

link = "https://www.amazon.fr/Playstation-CFI-1216A-5-Standard-Console/dp/B08H93ZRK9/?_encoding=UTF8&pd_rd_w=NI4aO&content-id=amzn1.sym.8900c35f-adfe-4944-865a-9134d5ab3571&pf_rd_p=8900c35f-adfe-4944-865a-9134d5ab3571&pf_rd_r=62MZSWJFS4CPRD21D1FB&pd_rd_wg=HF44S&pd_rd_r=87e8f08e-7345-453d-862e-26489071690e&ref_=pd_gw_crs_zg_bs_530490&th=1"

reponse = requests.get(url= link, headers= headers)
web_page = reponse.text

soup = BeautifulSoup(web_page, "html.parser")
price = soup.select("span.a-price:nth-child(2) > span:nth-child(1)")[0].getText().split("€")[0]
print(f" Price = {price}")
converted =float(price.replace(",","."))
if converted < 600:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        msg = f"The price of the PS  is {price}"
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail, to_addrs="baba78122@gmail.com", msg=f"Subject:PS5 price break\n\n {msg}")