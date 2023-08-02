import requests

from bs4 import BeautifulSoup

url="https://www.bbc.com/news"
response=requests.get(url)

if response.status_code == 200:
    soup=BeautifulSoup(response.text, "html.parser")
    headline_list=[]

    headlines=soup.find_all("h3", class_="gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text")

    for headline in headlines:
        headline_list.append(headline.text)
    print(headline_list)
else:
    print("это неверно")