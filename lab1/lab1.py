# Львівський національний університет імені Івана Франка
# Посилання: https://lnu.edu.ua/

from requests import get
from bs4 import BeautifulSoup

URL = "https://lnu.edu.ua/about/faculties/"
page = get(URL)
soup = BeautifulSoup(page.content,  "html.parser")

with open("lnu.txt", "w", encoding="UTF=8") as file:
    fac_list = soup.find(class_="structural-units")
    for li in fac_list.find_all("li"):
        
        h2 = li.find("h2")
        a = li.find("a")
        link = a.get("href")
        fac_name = h2.find(text=True, recursive=False)
        file.write(f"{fac_name} - {link}\n")
        print(fac_name)
        print(link)
