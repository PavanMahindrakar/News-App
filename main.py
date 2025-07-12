import requests

query = input("What type of news you want to read?\nNews Of: ")

API = "4e6e793227aa49cfb0ff1d551191ef57"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-07-11&to=2025-07-11&sortBy=popularity&apiKey={API}"
# print(url)

r = requests.get(url)
data = r.json()

articles = data["articles"]

for index, article in enumerate(articles):
    print(f"\nArticle No. {index + 1}:")
    print(f"Title: {article['title']}\nauthor: {article['author']}\nurl: {article['url']} ")
    print("-" * 180)  # Separator for readability