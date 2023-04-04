from bs4 import BeautifulSoup
from selenium import webdriver
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

driver = webdriver.chrome
driver.get(URL)
driver.implicitly_wait(10)
html = driver.page_source
# response = requests.get(URL)
# empire_online = response.text

soup = BeautifulSoup(html, "html.parser")
movie_list = soup.select("article")




print(movie_list)

