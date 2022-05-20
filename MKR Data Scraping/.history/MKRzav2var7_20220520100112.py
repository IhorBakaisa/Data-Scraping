# Посилання: https://ek.ua/ua/list/91/

from requests import get
from bs4 import BeautifulSoup

URL = "https://ek.ua/ua/list/91/"

page = get(URL)
soup = BeautifulSoup(page.content,  "html.parser")

with open("univ_kiev.txt", "w", encoding="UTF=8") as file:
    prod_list = soup.find(id_="list_form1")
    for div in prod_list.find_all("div"):
        
        table = div.find("table")
        td = table.find("td")
        a = td.find("a")
        prod_name = a.find(text=True, recursive=False)
        file.write(f"{prod_name}")
        print(prod_name)