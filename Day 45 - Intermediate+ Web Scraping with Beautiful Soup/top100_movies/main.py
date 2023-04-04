from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(
    URL,
)
empire_online = response.text

soup = BeautifulSoup(empire_online, "html.parser")
movie_list = soup.select_one("h3 .jsx-4245974604")
print(movie_list)
