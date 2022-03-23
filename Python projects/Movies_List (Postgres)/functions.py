from model import MoviesModel
from datetime import datetime


def register_user():
    username=input("Choose Username")
    MoviesModel.register_user(username)


def add_movie_flow():
    movie_name = input("What's the movie?: ")
    movie_date = input("And the release_date?[dd-mm-YY]:  ")
    MoviesModel.insert_movie(movie_name, movie_date)


def upcoming_movies_flow():
    result = MoviesModel.get_movies(upcoming=True)
    print("-----\n")
    for movie in result:
        date = datetime.fromtimestamp(movie[1]).strftime("%b %d %Y")
        print(movie[0], date)
    print("---- \n \n")


def all_movies_flow():
    result = MoviesModel.get_movies(upcoming=False)
    for movie in result:
        date = datetime.fromtimestamp(movie[1]).strftime("%b %d %Y")
        print(movie[0], date)
    print("---- \n \n")


def watched_movie_flow():
    movie = input("Which movie have you watched already? ")
    username= input("Whats your Username? ")
    MoviesModel.mark_watched(username=username,movie=movie)


def all_watched_flow():
    username=input("Your username please")
    result = MoviesModel.get_watched(username)
    print("-----\n\n")
    for movie in result:
        date = datetime.fromtimestamp(movie[1]).strftime("%b %d %Y")
        print(movie[0], date)
    print("---- \n \n")