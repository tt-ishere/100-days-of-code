from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# article_tag = soup.select(".titleline a")
# article_text = article_tag.string
# article_link = article_tag.get("href")
# article_vote_tag = soup.find(name="span", id="score_35343495")
# article_vote = article_vote_tag.get_text()


# with open(file="Bs4-start/website.html", encoding="cp437") as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, "html.parser")

# # methods - find all
# links = soup.find_all(name="a")
# for link in links:
#     # print(link.string) #gets just the string from the tag
#     # print(link.get("href")) #get by attributes

# heading_sect = soup.find_all(name="h3", class_="heading")
# new_heading = [x.getText() for x in heading_sect]
# print(new_heading)

# # using tag selectors
# company_url = soup.select_one("p a")
# print(company_url.get("href"))

# # using attribute selectors
# name = soup.select_one("#name") #select by id
# print(name)

# heading_container = soup.select(".heading") #select by class
# print(heading_container)
