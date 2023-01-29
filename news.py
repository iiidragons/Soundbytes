import re 
import requests
from bs4 import BeautifulSoup
import random




def scrape_text(url, source):
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(url, source)

    if source == "cnn":
        tags = soup.find(string=re.compile(r'"articleBody":"(.*?)","author":'))
        match = re.search(r'"articleBody":"(.*?)","author":', str(tags))
        if match:
           article_text = match.group(1)
           return article_text
    elif source == "fox-news":
      text = soup.find(string=re.compile(r'"articleBody": "(.*?)",'))
      print(text)
      match = re.search(r'"articleBody": "(.*?)",', str(text))
      if match:
          article_text = match.group(1).replace("&nbsp;", "").replace('\\', '')
          return article_text
    elif source == "bbc-news":
      bodies = soup.find_all(attrs={'class':'ssrcss-11r1m41-RichTextComponentWrapper'})
      text = []
      for body in bodies:
          text += [p.text.replace("\\", "") for p in body.find_all("p")] 
      article_text = ' '.join(text)
      return article_text
      
    #return text


def get_news(topic, source):
    articles = []
    combined_text = []
    counter=0
    print(source)
    if source == "random":
      source = random.choice(["CNN", "FOX", "BBC"])
    dic = {
        "CNN": "cnn",
        "FOX": "fox-news",
        "BBC": "bbc-news"
    }
    source = dic[source]
    print(source+"1")
    api_key = "cb5c8c71142c4ea0b6c891574c8dc84a"
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}&sortBy=top&sources={source}"
    response = requests.get(url)
    data = response.json()
  
    for article in data["articles"]:
        if counter >= 1:
          break
        text = scrape_text(article["url"], source)
        combined_text.append(text)
        print(text)
        articles.append({
            "url": article["url"],
            "text": text
        })
      
        counter += 1
    return articles, combined_text