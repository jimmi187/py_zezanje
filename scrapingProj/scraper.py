import requests
from bs4 import BeautifulSoup
from pprint import pprint
from time import sleep
from random import choice
from csv import DictWriter, DictReader


base_url ="http://quotes.toscrape.com"


def scrape():
    def ucitaj():
        with open("scrapingProj/data.csv",encoding="utf-8") as file:
            csv_reader = DictReader(file)
            for row in csv_reader:
                all_quotes.append(row)    
    all_quotes = []
    url = "/page/1/"
    ucitaj()
    if not all_quotes:
        while url:
            res = requests.get(f"{base_url}{url}")
            print(f"Now scraping {base_url}{url}")
            soup = BeautifulSoup(res.text, "html.parser")
            quotes = soup.find_all(class_="quote")

            for q in quotes:
                all_quotes.append({
                    "text": q.find(class_="text").text,
                    "author" : q.find(class_="author").text, 
                    "bio-link" : q.find("a", href=True)["href"]  
                })

            next_btn = soup.find(class_="next")
            url = next_btn.find("a", href=True)["href"] if next_btn else None

        with open("scrapingProj/data.csv", "w", encoding="utf-8", newline='') as file:
            headers = ["text", "author", "bio-link"]
            csv_writer = DictWriter(file, fieldnames=headers)
            csv_writer.writeheader()
            csv_writer.writerows(all_quotes)

        ucitaj()
    return all_quotes


def play_game(quotes):
    ch = choice(quotes)
    quote = ch["text"]
    name = ch["author"]   
    link = ch["bio-link"]
    soup = BeautifulSoup(requests.get(f"{base_url}{link}").text, "html.parser")
    born_date = soup.find(class_="author-born-date").get_text()
    born_location = soup.find(class_="author-born-location").get_text()

    print(f'here is a quete:\n {quote}\n')
    remaining_guesses = 4
    guess = ''
    while guess.lower() != name.lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? Remaining guesses: {remaining_guesses}")
        if guess.lower() == name.lower():
            print("u got it right!")
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            print("Here's a hint: The author was born on {} at {}".format(born_date, born_location))
        elif remaining_guesses == 2:
            print("Here's a hint: first letter of the name => "+name[0:1] )
        elif remaining_guesses == 1:
            last_name = name.split(" ")[1][0]
            print(f"Here's a hint: initials => {name[0]}.{last_name}.")
        else:
            print(f"You have lost the game, here is a solution to the question {name}")

    again = ''
    while again.lower() not in ('yes','y','no',"n"):
        again = input("Would you like to play again (y/n)")
    if again.lower() in ('yes','y'):
        return play_game(quotes)
    else:
        print("OK, goodbye!")


v = scrape()
play_game(v)
