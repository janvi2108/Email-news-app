import requests
api_key="f7125a28116e48a2b93936584bc30b7d"
url="https://newsapi.org/v2/everything?q=tesla&from=2025-07-05&sortBy=publishedAt&apiKey=f7125a28116e48a2b93936584bc30b7d"

#request
request=requests.get(url)

#get dictionary with data
content=request.json()

#accessing article title and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

