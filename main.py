from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
web_page =response.text

soup =BeautifulSoup(web_page,"html.parser")
all_anchor = soup.select(".titleline a[rel]")
titles = [elt.getText() for elt in all_anchor]
links = [elt.get("href") for elt in all_anchor]
scores = soup.findAll(name= "span", class_ = "score")
print(links)

soup.select(".nowrap a")

# with open("website.html",encoding='utf8') as file:
#     content = file.read()
#
# soup = BeautifulSoup(content,'html.parser')
# all_anchor = soup.select("a")
# print(all_anchor)
# for a in all_anchor:
#     print(a.get("href"))