from tkinter import*
from BookStore_Back import *

window=Tk()
window.title("BookStore")
window.geometry("500x500")

db=DB_operations
db().create_table()

#WE ARE DEFINING FUNCS CONTAINING CLASS INSTANCES BECAUSE WE WANT TO CALL THEM LATER WITH
#THE VARIABLES, DIRECT CLASS INSTANTIATION IN THE BEGINNING RETURNS AN ERROR - NAME ERROR - VARIABLE NOT DEFINED

def search():
    db1=db(e1_value.get(),e2_value.get(),e_1_value.get(),e_2_value.get())
    lst1.delete(0,END)
    iterate=0
    for n in db1.search_db():
        iterate+=1
        lst1.insert(END,f"{iterate}"+" "+ f"{n}")
def view():
    lst1.delete(0,END)
    iterate=0
    for n in db().view_all():
        iterate+=1
        lst1.insert(END,f"{iterate}"+" "+ f"{n}")
def insert():
    db1=db(e1_value.get(),e2_value.get(),e_1_value.get(),e_2_value.get())
    db1.insert_db()
def update():
    db1=db(e1_value.get(),e2_value.get(),e_1_value.get(),e_2_value.get())
    db1.update_table()
def delete_table():
    db1=db(e1_value.get(),e2_value.get(),e_1_value.get(),e_2_value.get())
    db1.delete_table()
def delete_all():
    lst1.delete(0,END)
    db().delete_all()





l1=Label(text="Title",height=1,width=3,font=(None,10,"italic"))
l1.grid(row=0,column=0,pady=5,padx=10)

l2=Label(text="Year",height=1,width=3,font=(None,10,"italic"))
l2.grid(row=1,column=0,pady=5,padx=10)

#StringVar() is a special Tkinter object that acts as a container that stores whatever it is being passed, here it is from the textvariable parameter in Entry().
e1_value=StringVar()
e1=Entry(window,width=22,textvariable=e1_value)
e1.insert(0,"Choose title")
e1.grid(row=0,column=1,pady=2,padx=15)

e2_value=StringVar()
e2=Entry(window,width=22,textvariable=e2_value)
e2.insert(0,"Choose Year")
e2.grid(row=1,column=1,pady=2,padx=15)

l_1=Label(text="Author",height=1,width=4,font=(None,10,"italic"))
l_1.grid(row=0,column=2,pady=5,padx=7)

l_2=Label(text="ISBN",height=1,width=6,font=(None,10,"italic"))
l_2.grid(row=1,column=2,pady=5,padx=7)

e_1_value=StringVar()
e_1=Entry(window,width=22,textvariable=e_1_value)
e_1.insert(0,"Choose Author")
e_1.grid(row=0,column=3,pady=2,padx=12)

e_2_value=StringVar()
e_2=Entry(window,width=22,textvariable=e_2_value)
e_2.insert(0,"Choose ID")
e_2.grid(row=1,column=3,pady=2,padx=12)





f1=Frame(window)
f1.grid(row=2,column=0,columnspan=3,pady=10,padx=3)

sc1=Scrollbar(f1)
sc1.grid(row=0,column=3,padx=5,sticky="ns")

sc2=Scrollbar(f1,orient="horizontal")
sc2.grid(row=1,column=0,columnspan=2,padx=5,sticky="ew")

lst1=Listbox(f1,width=28,height=12,yscrollcommand=sc1.set,xscrollcommand=sc2.set)
lst1.grid(row=0,column=0,columnspan=2,pady=40,padx=3)
sc1.config(command = lst1.yview)
sc2.config(command = lst1.xview)

f2=LabelFrame(window,text="Commands")
f2.grid(row=2,column=3)





b1=Button(f2,text='View All',width=14,height=1,command=view)
b1.grid(row=0,column=0,pady=3)

b2=Button(f2,text='Search Entry',width=14,height=1,command=search)
b2.grid(row=1,column=0,pady=3)

b3=Button(f2,text='Add Entry',width=14,height=1,command=insert)
b3.grid(row=2,column=0,pady=3)

b4=Button(f2,text='Update Selected',width=14,height=1,command=update)
b4.grid(row=3,column=0,pady=3)

b5=Button(f2,text='Delete Selected',width=14,height=1,command=delete_table)
b5.grid(row=4,column=0,pady=3)

b6=Button(f2,text='Close',width=14,height=1,command=window.destroy)
b6.grid(row=5,column=0,pady=3)

b6=Button(window,text='DELETE ALL',width=14,height=1,command=delete_all)
b6.grid(row=3,column=1,pady=3)





window.mainloop()




## IN THE TERMINAL AFTER INSTALLING (PIP PYINSTALLER) WE TYPE "pyinstaller --onefile --windowed BookStore_Front.py"
# AND THIS WAY WE CREATE AN .EXE FILE THAT OTHERS CAN USE
# WE PUT ONLY THE MAIN SCRIPT(BookStore_Front.py), THAT IS REFRENCING TO ALL THE OTHER SCRIPTS