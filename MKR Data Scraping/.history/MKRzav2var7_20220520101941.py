# Посилання: https://ek.ua/ua/list/91/

from requests import get
from bs4 import BeautifulSoup

URL = "https://ek.ua/ua/list/91/"

page = get(URL)
soup = BeautifulSoup(page.content,  "html.parser")

with open("univ_kiev.txt", "w", encoding="UTF=8") as file:
    prod_list = soup.find(class_="main-part-content")
    form = prod_list.find("form")
    for div in form.find_all("div"):
        a = div.find("a")
        file.write(f"{a}")
        print(a)
     