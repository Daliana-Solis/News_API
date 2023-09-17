import requests

#get API key from newsapi.org
api_key = "a89c2640956b432db3113b5ff5697abb"

#get news from this api (tesla)
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-08-17"\
      "&sortBy=publishedAt&apiKey=a89c2640956b432db3113b5ff5697abb"

#request data from this url
request = requests.get(url)

#get content, turn it into json (dict)
content = request.json()

#list of articles (dictionaries) inside content
#dictionary has source, author, title, desc, url.....
for article in content["articles"]:
      print(article["title"])