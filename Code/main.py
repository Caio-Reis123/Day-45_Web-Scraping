from turtle import st
import requests
from bs4 import BeautifulSoup as bs

URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(URL)

web_page = response.text

soup = bs(web_page, 'html.parser')

movies = []

titles = soup.find_all(name='h3', class_='title')
for title_tag in titles:
    title_text = title_tag.get_text()
    movies.append(title_text)


reversed_movies = movies[::-1]


print(reversed_movies)

with open ('movies.txt', 'w') as output:
    for movie in reversed_movies:
        output.write(f'{movie}\n')