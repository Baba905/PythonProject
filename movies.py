from bs4 import BeautifulSoup
import requests

reponse = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = reponse.text



soup = BeautifulSoup(web_page, "html.parser")
h3_tag = soup.select(".article-title-description__text h3")
movies_titles = [elt.getText() for elt in h3_tag[-1::-1]]

file = open("movies.txt","a", encoding="utf8")
for title in movies_titles:
    tmp = f"{title}\n"
    file.write(tmp)
file.close()