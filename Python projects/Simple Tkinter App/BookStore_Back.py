import sqlite3


### THIS IS NOT THE MOST OPTIMIZED AND CLEAN WAY TO WRITE THE CLASS - CHECK "BookStore_Back_optimized" FILE - TO SEE HOW TO MAKE IT EVEN CLEANER 


class DB_operations():

    def __init__(self,title=None,year=None,author=None,isbn=None):

        self.title=title
        self.year=year
        self.author=author
        self.isbn=isbn


    def create_table(self):
        db=sqlite3.connect("Book_DB.db")
        cur=db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS books(title TEXT, year TEXT, author TEXT, isbn TEXT)")
        db.commit()
        db.close()

    
    def insert_db(self):
        db=sqlite3.connect("Book_DB.db")
        cur=db.cursor()
        cur.execute("INSERT INTO books VALUES(?,?,?,?)",( self.title,self.year,self.author,self.isbn))
        db.commit()
        db.close()


    def search_db(self):
        db=sqlite3.connect("Book_DB.db")
        cur=db.cursor()
        #DISTINCT DELETES DUPLICATE ROWS AND LEAVES ONLY ONE INSTANCE
        cur.execute("SELECT DISTINCT title,year,author,isbn FROM books WHERE title=? OR year=? OR author=? OR isbn=?",( self.title,self.year,self.author,self.isbn))
        view=cur.fetchall()
        return view
        db.close()

    def view_all(self):
        db=sqlite3.connect("Book_DB.db")
        cur=db.cursor()
        #DISTINCT DELETES DUPLICATE ROWS AND LEAVES ONLY ONE INSTANCE
        cur.execute('SELECT DISTINCT title,year,author,isbn FROM books')
        view=cur.fetchall()
        return view
        db.close()

    def update_table(self):
        db=sqlite3.connect("Book_DB.db")
        cur=db.cursor()
        while True:
            try:
                cur.execute("UPDATE books SET title=?, year=?, author=?, isbn=? WHERE isbn=?",( self.title,self.year,self.author,self.isbn,self.isbn))
                break
            except:
                print("Please enter a valid ISBN")
        db.commit()
        db.close()

    def delete_table(self):
        db=sqlite3.connect("Book_DB.db")
        cur=db.cursor()
        #DELETES THE ENTIRE ROW
        cur.execute("DELETE FROM books WHERE isbn=?",(self.isbn,))
        db.commit()
        db.close()

    def delete_all(self):
        db=sqlite3.connect("Book_DB.db")
        cur=db.cursor()
        #DELETES EVERYTHING
        cur.execute("DELETE FROM books")
        db.commit()
        db.close()


        
    


#db=DB_operations("Toshko",2008,"manga","1232421561")
#db.insert_db()
#db=DB_operations("Harry Potter",2002,"J.K.Rowling","1232421540")
    
