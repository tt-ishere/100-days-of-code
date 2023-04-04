from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.select(".titleline a")
# print(articles.string)
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_vote = [
    int(score.get_text()[0].split(" ")[0])
    for score in soup.find_all(name="span", class_="score")
]
# print(article_texts)
# print(article_links)
print(article_vote)
