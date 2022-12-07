import csv

from bs4 import BeautifulSoup

import requests


def gettop250():
    fields = ['Movie Name', 'Poster url', 'Released year', 'Rating']

    with open('Top250.csv', 'w', newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(fields)
        http_text = requests.get('https://www.imdb.com/chart/top/?sort=rk,asc&mode=simple&page=1').text
        soup = BeautifulSoup(http_text, 'lxml')
        movies_list = soup.find_all('tr')
        for movie_data in movies_list:
            roww = []
            if movie_data.a:
                movie_name = movie_data.find('img')['alt']
                roww.append(movie_name)
                poster_url = movie_data.find('img')['src']
                roww.append(poster_url)
                movie_release_year = movie_data.find('span', class_='secondaryInfo').text
                roww.append(movie_release_year[1:-1])
                movie_rating = movie_data.find('strong').text
                roww.append(movie_rating)
                csvwriter.writerow(roww)
            else:
                continue


if __name__ == '__main__':
    gettop250()
    print('Got it!')
