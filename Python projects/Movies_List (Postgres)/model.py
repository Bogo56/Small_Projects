import psycopg2
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()


class MoviesModel:

    connection = psycopg2.connect(
        host="localhost",
        database="movies",
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASS"]
    )



    @classmethod
    def create_table_movies(cls):
        with cls.connection as con:
            with con.cursor() as cur:
                cur.execute('CREATE TABLE IF NOT EXISTS movies(movie_name TEXT UNIQUE, release_date REAL);')


    @classmethod
    def create_table_users(cls):
        with cls.connection as con:
            with con.cursor() as cur:
                cur.execute("CREATE TABLE IF NOT EXISTS users( user_id SERIAL PRIMARY KEY, user_name TEXT UNIQUE);")


    @classmethod
    def create_table_watched(cls):
        with cls.connection as con:
            with con.cursor() as cur:
                cur.execute('CREATE TABLE IF NOT EXISTS watched( username TEXT,'
                        ' movie_name TEXT,'
                        'FOREIGN KEY(username) REFERENCES users(user_name),'
                        'FOREIGN KEY(movie_name) REFERENCES movies(movie_name));')


    @classmethod
    def register_user(cls,user_name):
        with cls.connection as con:
            with con.cursor() as cur:
                cur.execute("INSERT INTO users(user_name) VALUES (%s);",(user_name,))


    @classmethod
    def insert_movie(cls,movie_name,date):
        with cls.connection as con:
            with con.cursor() as cur:
                date=datetime.strptime(date,"%d-%m-%Y")
                timestamp=datetime.timestamp(date)
                cur.execute('INSERT INTO movies VALUES (%s,%s);',(movie_name,timestamp))


    @classmethod
    def get_movies(cls,upcoming=False):

        if upcoming:
            with cls.connection as con:
                with con.cursor() as cur:
                    today=datetime.today()
                    date_stamp=datetime.timestamp(today)
                    cur.execute('SELECT * FROM movies WHERE release_date > %s;',(date_stamp,))
                    res=cur.fetchall()
                    return res
        else:
            with cls.connection as con:
                with con.cursor() as cur:
                    cur.execute("SELECT * FROM movies")
                    res=cur.fetchall()
                    return res

    @classmethod
    def mark_watched(cls,movie,username):
        with cls.connection as con:
            with con.cursor() as cur:
                cur.execute("SELECT * FROM users WHERE user_name=%s;",(username,))
                check_user = cur.fetchone()
                cur.execute("SELECT * FROM movies WHERE movie_name=%s;", (movie,))
                check_movie = cur.fetchone()
                if not check_user:
                    print("No such Username \n\n")
                if check_movie and check_user:
                    cur.execute("INSERT INTO watched VALUES (%s,%s);",(username,movie))
                    print ("Update successful \n\n")
                else:
                    print("We don't have that movie \n\n")

    @classmethod
    def get_watched(cls,username):
        with cls.connection as con:
            with con.cursor() as cur:
                cur.execute("SELECT movies.movie_name,movies.release_date FROM movies JOIN watched ON "
                            "movies.movie_name=watched.movie_name WHERE username=%s;",(username,))
                res = cur.fetchall()
                return res
