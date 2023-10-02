import requests
from send_email import send_email

topic = "tesla"

#get API key from newsapi.org
api_key = "API KEY HERE"

#get news from this api ()
url = "https://newsapi.org/v2/everything?"\
      f"q={topic}&"\
      "from=2023-08-17"\
      "&sortBy=publishedAt&"\
      "apiKey=a89c2640956b432db3113b5ff5697abb"\
      "&language=en" #only articles in engligh

#request data from this url
request = requests.get(url)

#get content, turn it into json (dict)
content = request.json()

#list of articles (dictionaries) inside content, limit to 20
#dictionary has source, author, title, desc, url.....

body = ""
for article in content["articles"][:20]:
      if article["title"] is not None:
            body = "Subject: Today's news" + "\n" + body + article["title"] +\
                    "\n" + article["description"] + "\n" +\
                    article["url"] + 2*"\n"



body = body.encode("utf-8")
send_email(body)