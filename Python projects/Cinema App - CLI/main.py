import sqlite3
import random
from visitor import Visitor
from seats import Seats



##I CREATED THIS CLASS JUST FOR THE SAKE OF USING OOP,
# I'M NOT REALLY SURE IF THIS IS PROCEDURAL APPROACH WOULDN'T BE BETTER##

class Theater:

    def __init__(self, visitor, free_seats):
        self.free_seats = free_seats
        self.visitor=visitor

    def initiate_payment(self):

        self._seats_taken=[]

        seat = input(f"These are the free seats: {list(self.free_seats.keys())}. Choose One: ")
        ask_to_pay = input(f"The price for {seat} is {self.free_seats[seat]}. Do you take it? Y/N: ").upper()

        if ask_to_pay == "Y":
            self.visitor.pay(self.free_seats[seat])
            self._seats_taken.append(seat)
        elif ask_to_pay == "N":
            while True:
                ask_again = input("Do you want another seat Y/N: ").upper()
                if ask_again == "N":
                    print('Thank You. Have a Good Day!')
                    break
                if ask_again == "Y":
                    seat = input(f"These are the free seats: {list(self.free_seats.keys())}")
                    ask_to_pay = input(f"The price for {seat} is {self.free_seats[seat]} BGN.Do you take it? Y/N: ").upper()
                    if ask_to_pay == "N":
                        continue
                    else:
                        self.visitor.pay(self.free_seats[seat])
                        self._seats_taken.append(seat)

        return self._seats_taken


    def seats_taken(self):
        if len(self._seats_taken)==0:
            return "No Seats Taken"
        else:
            return self._seats_taken





name=input("What's your name:  ")
card= input("What's your card:  ")
balance=random.choice(list(range(1000,10000,500)))
mail=input("And finally your mail please:  ")

visitor1=Visitor(name=name,card=card,mail=mail,balance=balance)
visitor1.register()
seats=Seats()
available_seats=seats.availability()


BroadWay=Theater(visitor1,available_seats)
BroadWay.initiate_payment()
seats_taken=BroadWay.seats_taken()

for n in seats_taken:
    seats.update_status(n)


print("Balance left on Card:",visitor1.checking_balance())


