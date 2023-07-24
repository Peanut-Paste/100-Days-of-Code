import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

top100 = [i.getText() for i in soup.find_all("h3", class_="title")]


with open("movies.txt", mode="a", encoding="utf-8") as file:
    for movies in top100[::-1]:
        file.write(movies + "\n")
