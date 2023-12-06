import  requests
from bs4 import BeautifulSoup

class__ = "c-title.a-no-trucate.a-font-primary-bold-s.u-letter-spacing-0021.u-font-size-23\@tablet.lrv-u-font-size-16.u-line-height-125.u-line-height-normal\@mobile-max.a-truncate-ellipsis.u-max-width-245.u-max-width-230\@tablet-only.u-letter-spacing-0028\@tablet"
class_ = "c-title.a-no-trucate.a-font-primary-bold-s.u-letter-spacing-0021.lrv-u-font-size-18\@tablet.lrv-u-font-size-16.u-line-height-125.u-line-height-normal\@mobile-max.a-truncate-ellipsis.u-max-width-330.u-max-width-230\@tablet-only"


def scrapping(link_request):
    response = requests.get(url=link_request)
    web_page = response.text
    soup = BeautifulSoup(web_page, 'html.parser')
    h3_tag = soup.select(f"h3#title-of-a-story.{class__}")
    song_title =[elt.getText().replace('\n',"").replace('\t',"") for elt in h3_tag]
    for h3 in soup.select(f"h3#title-of-a-story.{class_}"):
        tmp = h3.getText().replace('\n',"").replace('\t',"")
        song_title.append(tmp)
    return song_title