# Посилання: https://ek.ua/ua/list/91/

from distutils.spawn import spawn
from requests import get
from bs4 import BeautifulSoup

URL = "https://ek.ua/ua/list/91/"

page = get(URL)
soup = BeautifulSoup(page.content,  "html.parser")

with open("univ_kiev.txt", "w", encoding="UTF=8") as file:
    prod_list = soup.find(class_="main-part-content")
    form = prod_list.find("form")
    for div in form.find_all("div"):
        table = div.find("table")
        tr = table.find("tr")
        table1 = tr.find("table")
        a = table1.find("a")
        name_a = a.find(text=True, recursive=False)
        file.write(f"{name_a}")
        print(name_a)
     