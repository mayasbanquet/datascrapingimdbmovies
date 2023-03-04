import requests 
from bs4 import BeautifulSoup
import pandas as pd 

url = 'https://www.imdb.com/chart/top'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('tbody', {'class': 'lister-list'})
rows = table.find_all('tr')

movies = []

for row in rows:
    title = row.find('td', {'class': 'titleColumn'}).a.text
    year = row.find('td', {'class': 'titleColumn'}).span.text.strip('()')
    rating = row.find('td', {'class': 'ratingColumn imdbRating'}).strong.text
    
    movies.append({'title': title, 'year': year, 'rating': rating})

df = pd.DataFrame(movies)

df.to_csv('/Users/rafaelbarbaroto/Desktop/imdb_top250.csv', index=False)