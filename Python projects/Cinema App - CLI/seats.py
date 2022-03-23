import sqlite3
import random


class Seats:


    def availability(self):
        conn=sqlite3.connect("database.db")
        cur=conn.cursor()
        cur.execute("SELECT seat_num,price FROM seats WHERE taken=0")
        result=cur.fetchall()
        seats={}
        for seat,price in result:
            seats[seat]=price
        conn.close()
        return seats

    def update_status(self,seat_num):
        seat_num=seat_num.upper()
        conn=sqlite3.connect("database.db")
        cur=conn.cursor()
        cur.execute("UPDATE seats SET taken=1 WHERE seat_num=?",[seat_num])
        conn.commit()
        conn.close()



# conn=sqlite3.connect('database.db')
# cur=conn.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS seats(seat_num TEXT UNIQUE,taken INTEGER,price INTEGER")
# cur.executemany("INSERT INTO seats(seat_num,taken,price) VALUES(?,?,?)",seat_combination)
# conn.commit()
# conn.close()
#
#
#
# print(seats)
# print()
# print(seat_combination)

if  __name__=="__main__":

    test=Seats().availability()
    update=Seats().update_status("a1")
    print(test)
