import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

page_content = BeautifulSoup(response.text, 'html.parser')

titles = page_content.find_all(name = "h3", class_ = "listicleItem_listicle-item__title__BfenH")

movie_list = []

for title in titles:
    movie_list.append([int((title.getText().split(" ")[0]).replace(")", "")),  
                       title.getText()])
    
movie_list.sort()
movie_list = [movie[1] for movie in movie_list]

with open("movies.txt", mode = "w", encoding = "utf8") as movie_file:
    movie_file.write('\n'.join(movie_list, ))

with open("movies.txt", mode = "r", encoding = "utf8") as movie_file:
    print(movie_file.read())