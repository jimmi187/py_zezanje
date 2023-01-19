import requests
from bs4 import BeautifulSoup
from time import sleep


base_url = "https://tekstovi.net/2,87,4058.html"

res = requests.get(base_url)
soup = BeautifulSoup(res.text, "html.parser")
texts = soup.find_all(class_="lyric")
text = ""
for i in texts:
    text += i.get_text()
    
print(text)