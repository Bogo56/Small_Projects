import sqlite3

## THIS IS ANOTHER ALTERNATIVE THAT IS CLEANER BUTT INCLUDES SOME PARTS THAT I'M NOT QUITE SURE
## SO TAKE THIS AS AN IDEA,INSPIRATION HOW YOU CAN ALSO DO IT - BUT BE AWARE THAT IT MIGH NOT BE THE BEST PRACTISE


class DB_operations():



    ## __init__ METHOD IS CALLING EVERYTHING THAT IS IN IT UPON INSTANTIATING OF AN OBJECT, WITHOT CALLING IT EXCPLICITLY AS THE OTHER METHODS. THIS IS WHY WE PUT DATABASE CONNECTION ONLY HERE
    def __init__(self,title=None,year=None,author=None,isbn=None):

        self.title=title
        self.year=year
        self.author=author
        self.isbn=isbn

        self.db=sqlite3.connect("Book_DB.db")
        self.cur=self.db.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books(title TEXT, year TEXT, author TEXT, isbn TEXT)")
        self.db.commit()


    
    
    def insert_db(self):     
        self.cur.execute("INSERT INTO books VALUES(?,?,?,?)",( self.title,self.year,self.author,self.isbn))
        self.db.commit()
        


    def search_db(self):
        #DISTINCT DELETES DUPLICATE ROWS AND LEAVES ONLY ONE INSTANCE
        self.cur.execute("SELECT DISTINCT title,year,author,isbn FROM books WHERE title=? OR year=? OR author=? OR isbn=?",( self.title,self.year,self.author,self.isbn))
        view=self.cur.fetchall()
        return view
    

    def view_all(self):
        #DISTINCT DELETES DUPLICATE ROWS AND LEAVES ONLY ONE INSTANCE
        self.cur.execute('SELECT DISTINCT title,year,author,isbn FROM books')
        view=self.cur.fetchall()
        return view
     

    def update_table(self):
        while True:
            try:
                self.cur.execute("UPDATE books SET title=?, year=?, author=?, isbn=? WHERE isbn=?",( self.title,self.year,self.author,self.isbn,self.isbn))
                break
            except:
                print("Please enter a valid ISBN")
        self.db.commit()


    def delete_table(self):
        #DELETES THE ENTIRE ROW
        self.cur.execute("DELETE FROM books WHERE isbn=?",(self.isbn,))
        self.db.commit()
    

    def delete_all(self):
        #DELETES EVERYTHING
        self.cur.execute("DELETE FROM books")
        self.db.commit()
        

    ## __del__ WILL EXECUTE WHEN THE PROGRAM FINISHES. IT IS ACTUALLY  BEING USED IN RELATION TO "GARBAGE COLLECTION" IN PYTHON BUT IN THIS CASE IT CAN WORK AS WELL
    ## ANYWAY THIS METHOD IS RARELY USED SO KEEP THAT IN MIND

    def __del__(self):
        self.db.close()

        
    


