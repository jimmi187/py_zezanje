import requests
from random import choice



term = input("Let me tell you a joke! Give me a topic: ")

url = "https://icanhazdadjoke.com/search"
head = {"Accept": "text/plain"}
head2 = {"Accept": "application/json"}
qree  = {"term": term}
res = requests.get(url, headers=head2, params=qree).json()
# res.headers
# res.status_code
# print(res.text)
total_jokes = res["total_jokes"]
results = res["results"]

if total_jokes > 1:
    print(
        f"I've got {total_jokes} jokes about {term}. Here's one:\n",
        choice(results)['joke']
    )
elif total_jokes == 1:
    print(
        f"I've got one joke about {term}. Here it is:\n",
        results[0]['joke']
    )
else:
    print(f"Sorry, I don't have any jokes about {term}! Please try again.")
