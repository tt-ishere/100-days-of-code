from bs4 import BeautifulSoup
import requests

# URL of the web page we want to scrape
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Send a GET request to the URL and get the HTML content
response = requests.get(URL)
variety_web_page = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(variety_web_page, "html5lib")

# Select all the movie titles on the page using CSS selectors
movie_list = soup.select(
    ".listicle-container .listicle-item .listicle-item-content p a[href*='https://www.empireonline.com/movies/reviews']"
)

# Create a list to store the movie titles with their ranks
movies = []
movie_rank = 99
for movie in movie_list:
    # Extract the movie title from the text content of the <a> tag
    movie_line = movie.string.split("of ")
    movie_tittle = movie_line[1]

    # Add the movie title to the list with its rank
    tittle = f"{movie_rank}. {movie_tittle}"
    movies.append(tittle)

    # Decrease the movie rank for the next movie
    movie_rank -= 1

# Reverse the list of movies to rank them in ascending order
top_100_movies = movies[::-1]

# Write the list of movies to a text file
with open("top100_movies/movies.txt", "w") as file:
    for movie in top_100_movies:
        file.write(f"{movie}\n")
