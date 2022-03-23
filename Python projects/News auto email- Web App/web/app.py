from flask import Flask,render_template,request
from emailing_web import MailSender
import pandas
from datetime import datetime
from auto_mail import sched


app=Flask(__name__)

@app.before_first_request
def scheduler():
    sched.start()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/thank_you",methods=["POST"])
def sign_up():
    if request.method=="POST":
        e_mail=request.form['email']
        topic1,topic2,topic3=request.form["topic1"],request.form["topic2"],request.form["topic3"]
        topic_list=(topic1,topic2,topic3)
        topic_list= ",".join(topic_list).replace(",,",",")
        if topic_list[-1]==",":
            topic_list=topic_list[:-1]

        name,fname=request.form["name"],request.form["fname"]
        
        file="prospects-web/people.xlsx"

        df=pandas.read_excel(file)
        new_row={"name":name,"family_name":fname,"email":e_mail,"interest":topic_list, "date_appeared":datetime.now().strftime(f"%Y-%d-%m")}
        df=df.append(new_row,ignore_index=True)
        df.to_excel("prospects-web/people.xlsx",index=False)

        mailing = MailSender(e_mail)
        mailing.send_message(interest=topic_list,name=name)


    return render_template("thank_you.html",name=name,fname=fname,e_mail=e_mail)

        

if __name__=="__main__":
    app.run()


