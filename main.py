import requests
from send_email import send_email

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

body = ""
for article in content["articles"]:
      if article["title"] is not None:
            body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)