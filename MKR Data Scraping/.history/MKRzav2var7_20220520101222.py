# Посилання: https://ek.ua/ua/list/91/

from requests import get
from bs4 import BeautifulSoup

URL = "https://ek.ua/ua/list/91/"

page = get(URL)
soup = BeautifulSoup(page.content,  "html.parser")

with open("univ_kiev.txt", "w", encoding="UTF=8") as file:
    prod_list = soup.find(class_="model-short-block")
    for table in prod_list.find_all("table"):
        span = table.find("span")
        file.write(f"{span}")
        print(span)