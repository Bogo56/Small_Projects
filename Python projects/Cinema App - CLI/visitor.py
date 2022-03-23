
import sqlite3


##A  CLASS USED TO CHECK THE BALANCE OF A VISITOR. INSTEAD OF INHERITANCE I'M USING COMPOSITION HERE
# E.G A 'HAS A' RELATIONSHIP. THIS MEANS I'M INSTANTIATING IT IN ONE OF THE METHODS IN THE VISITORS CLASS##
class Balance:

    def __init__(self,email):
        self.email=email


    def check_balance(self):
        conn=sqlite3.connect("database.db")
        cur=conn.cursor()
        cur.execute("SELECT balance FROM visitors WHERE email=?",[self.email])
        balance=cur.fetchone()
        conn.commit()
        conn.close()
        return balance

    def update_balance(self,new_balance):
        conn=sqlite3.connect("database.db")
        cur=conn.cursor()
        cur.execute("UPDATE visitors SET balance=? WHERE email=?",[new_balance,self.email])
        cur.execute(("SELECT balance FROM visitors WHERE email=?"),[self.email])
        res=cur.fetchone()[0]
        conn.commit()
        conn.close()


class Visitor:

    def __init__(self,name,card,balance,mail):
        self.name=name
        self.card=card
        self.balance=balance
        self.mail=mail
##INSTANTIATING THE ABOVE BALANCE CLASS. USING _PRIVATE ATTRIBUTE BECAUSE IT IS NEEDED ONLY INSIDE
        # THE CLASS. THE CHECKING BALANCE SHOULD BE USED TO CHECK THE BALANCE NOT THE ATTRIBUTE
        # THAT'S ENCAPSULATION##
        self._money=Balance(self.mail)


    def register(self):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS visitors(name TEXT,card TEXT,balance REAL,email TEXT NOT NULL UNIQUE)")
        cur.execute("INSERT OR IGNORE INTO visitors(name,card,balance,email) VALUES(?,?,?,?)",
                    [self.name, self.card, self.balance, self.mail])
        conn.commit()
        conn.close()


    def checking_balance(self):
        balance=self._money.check_balance()
        balance=int(balance[0])
        return balance


    def pay(self,sum):
        if sum>self.checking_balance():
            print("Sorry, not enough money in your Balance")
        else:
            new_balance=self.checking_balance() - sum
            self._money.update_balance(new_balance)

##USING PROPERTY AS NOT TO ALLOW TO ASSIGN OTHER TYPES EXCEPT FOR INTEGER OR FLOAT
##CONCLUSION - PROPERTY IS ACTUALLY MAKING A FUNCTION CALLABLE AS AN ATTRIBUTE (E.G WITHOUT "()")
    #
    # SO HERE INSTEAD OF CALLING .balance() IT'S ENOUGH NOW TO CALL .balance  ##
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,value):
        if isinstance(value,(int,float)):
            self._balance=value
        else:
            raise ValueError("balance must be an integer or a float")







if __name__=="__main__":

    visitor=Visitor("bogo","master",50000,"b@b.com")
    visitor.register()
    a=visitor.checking_balance()
    visitor.pay(350)
    b=visitor.checking_balance()
    print("Initial Balance",a)
    print("New Balance",b)

