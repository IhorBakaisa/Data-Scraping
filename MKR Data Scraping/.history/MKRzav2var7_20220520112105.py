# Посилання: https://ek.ua/ua/list/91/

from json import dump
from requests import get
from bs4 import BeautifulSoup

URL = "https://ek.ua/ua/list/91/"

page = get(URL)
soup = BeautifulSoup(page.content,  "html.parser")

with open("list_prod.txt", "w", encoding="UTF=8") as file:
    prod_list = soup.find(class_="main-part-content")
    form = prod_list.find("form")
    for div in form.find_all("div"):
        u = soup.find(class_="u")
        name_u = u.find(text=True, recursive=False)
        file.write(f"{name_u}")
        print(name_u)
     