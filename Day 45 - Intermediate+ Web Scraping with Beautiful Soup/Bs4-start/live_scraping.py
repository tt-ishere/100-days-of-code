from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_texts = []
article_links = []

articles_line = soup.find_all(name="span", class_="titleline")
for article_span in articles_line:
    article_tag = article_span.find("a")

    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_votes = [
    int(score.get_text().split()[0])
    for score in soup.find_all(name="span", class_="score")
]

# finding the highest voted article
highest_article_votes = max(article_votes)
index_of_highest_article_votes = article_votes.index(highest_article_votes)

print(
    f"The story with the highest votes;\n\nTittle: {article_texts[index_of_highest_article_votes]}\nLink: {article_links[index_of_highest_article_votes]}"
)
