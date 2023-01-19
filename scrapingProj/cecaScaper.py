import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import DictWriter

base_url = "https://tekstovi.net/2,87,0.html"
lista_textova = []

res = requests.get(base_url)
soup = BeautifulSoup(res.text, "html.parser")
quotes = soup.find_all(class_="artLyrList")
for quote in quotes:
    url = quote.find("a",href=True)["href"][4:]
    sp = BeautifulSoup(requests.get(f"{base_url[:-7]}{url}").text, "html.parser")
    naslov = sp.find('h2', class_="lyricCapt").get_text()
    texts = sp.find_all(class_ = "lyric")
    print(f"Scraping {naslov}")
    text = ""
    for i in texts:
        text += i.get_text()
    lista_textova.append({
        'naslov': naslov,
        'text': text
    })


with open("scrapingProj/ceca.csv", "w", encoding="utf-8", newline='') as file:
    headers = ["naslov", "text"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerows(lista_textova)