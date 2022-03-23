from model import MoviesModel
from datetime import datetime
from functions import (add_movie_flow,
                       upcoming_movies_flow,
                       all_movies_flow,
                       watched_movie_flow,all_watched_flow,register_user)


menu = """Please select one of the following options:
0) Make Registration
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


MoviesModel.create_table_users()
MoviesModel.create_table_movies()
MoviesModel.create_table_watched()


print(welcome)

while True:
    print(menu)

    user_option = input("Tell us what you want to do?")

    if user_option == "6":
        break

    elif user_option == "0":
        register_user()

    elif user_option == "1":
        add_movie_flow()

    elif user_option == "2":
        upcoming_movies_flow()

    elif user_option == "3":
        all_movies_flow()

    elif user_option == "4":
        watched_movie_flow()

    elif user_option == "5":
        all_watched_flow()


    else:
        print("Please choose a number from 1 to 3")
        continue



print("Thank you, have a wonderful day !")






