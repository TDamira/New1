import requests
from bs4 import BeautifulSoup

url="https://myphone.kg/ru/catalog/cell"
response=requests.get(url)

if response.status_code ==200:
    soup=BeautifulSoup(response.text, "html.parser")
    name_list=[]
    names=soup.find_all("a")

    for name in names:
        name_list.append(name.text)
    print(name_list)

else:
    print("not found")

