import requests
from bs4 import BeautifulSoup
from csv import writer ,reader

res = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(res.text, "html.parser")
articles = soup.find_all("article")
with open("blog_data.csv", "w", newline='') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title","link","date"])
    for i in articles:
        a_tag = i.find("a")
        title = a_tag.get_text()
        url = a_tag["href"]
        date = i.find("time")["datetime"].split(" ")[0]
        csv_writer.writerow([title,url,date])

with open("blog_data.csv") as files:
    reder = reader(files)
    for k in reder:
        print(k)

    
