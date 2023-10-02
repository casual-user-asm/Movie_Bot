import requests
from bs4 import BeautifulSoup
import random


def top_250_movies():
    url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'}
    response = requests.get(url, headers=headers)
    src = response.text

    soup = BeautifulSoup(src, 'html.parser')

    titles_top_250 = soup.find_all('h3', class_='ipc-title__text')
    titles_list_250 = []
    for i in titles_top_250:
        titles_list_250.append(i.text)

    result = ''
    for i in titles_list_250[1:251]:
        result += i + '\n'

    return result


def popular_100_movies():
    url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'}
    response = requests.get(url, headers=headers)
    src = response.text

    soup = BeautifulSoup(src, 'html.parser')

    titles_top_100 = soup.find_all('h3', class_='ipc-title__text')
    titles_list_100 = []
    for i in titles_top_100:
        titles_list_100.append(i.text)

    count = 1
    result = ''
    for i in titles_list_100[1:101]:
        result += f"{count}. {i}\n"
        count += 1

    return result


def top_250_tv_shows():
    url = 'https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'}
    response = requests.get(url, headers=headers)
    src = response.text

    soup = BeautifulSoup(src, 'html.parser')

    titles_top_250_shows = soup.find_all('h3', class_='ipc-title__text')
    titles_list_250_shows = []
    for i in titles_top_250_shows:
        titles_list_250_shows.append(i.text)

    result = ''
    for i in titles_list_250_shows[1:251]:
        result += i + '\n'

    return result


def popular_100_tv_shows():
    url = 'https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'}
    response = requests.get(url, headers=headers)
    src = response.text

    soup = BeautifulSoup(src, 'html.parser')

    titles_top_100_shows = soup.find_all('h3', class_='ipc-title__text')
    titles_list_100_shows = []
    for i in titles_top_100_shows:
        titles_list_100_shows.append(i.text)

    count = 1
    result = ''
    for i in titles_list_100_shows[1:101]:
        result += f"{count}. {i}\n"
        count += 1

    return result


def random_top_250_movie(movies=top_250_movies()):
    new_list = movies.split('\n')
    random_number = random.randint(1, 250)
    return new_list[random_number]


def random_popular_100_movie(movies=popular_100_movies()):
    new_list = movies.split('\n')
    random_number = random.randint(1, 100)
    return new_list[random_number]


def random_top_250_tv_shows(shows=top_250_tv_shows()):
    new_list = shows.split('\n')
    random_number = random.randint(1, 250)
    return new_list[random_number]


def random_popular_100_tv_shows(shows=popular_100_tv_shows()):
    new_list = shows.split('\n')
    random_number = random.randint(1, 100)
    return new_list[random_number]
