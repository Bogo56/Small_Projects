from flask import Flask,render_template,request
from flask_sqlalchemy import *
from send_email import send_email
from sqlalchemy.sql import func

app=Flask(__name__)
##This is to connect to a local database
#app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:database_maistor345!@localhost/salary_survey"
app.config["SQLALCHEMY_DATABASE_URI"]=""


#Here we just define this class so that we can call it from the console and create table with columns in the DB
class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer,primary_key=True)
    email_=db.Column(db.String(120),unique=True)
    salary_=db.Column(db.Integer)

    def __init__(self,email_,salary_):
        self.salary_=salary_
        self.email_=email_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/thank_you",methods=['POST'])
def thank_you():
    if request.method=="POST":
        email=request.form["email_name"]
        salary=request.form["salary_name"]
        count=db.session.query(Data.salary_).count()
        if count>1:
            avg_salary=db.session.query(func.avg(Data.salary_)).scalar()
            avg_salary=round(avg_salary)
        if db.session.query(Data).filter(Data.email_==email).count()==0 and count>1:
            data=Data(email,salary)
            db.session.add(data)
            db.session.commit()
            send_email(email,salary,avg_salary,count)
            return render_template("thank-you.html")
        
        return render_template("index.html",text='Email already surveyed')

if __name__=="__main__":
    app.debug=True
    app.run()
