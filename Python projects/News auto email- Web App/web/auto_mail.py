import pandas
from emailing_web import MailSender
import time
from apscheduler.schedulers.blocking import BlockingScheduler


##This is the module for scheduling stuff
sched=BlockingScheduler()

# This is where we store the users info
file="prospects-web/people.xlsx"


##We will send your mail 2 times a day - at 10 and 20
@sched.scheduled_job("cron",day_of_week="mon-sun",hour=8)
def send_10():
    df = pandas.read_excel(file)
    for name, mail, topics in zip(set(df["name"]), set(df["email"]), set(df["interest"])):

        mailing=MailSender(mail)
        mailing.send_message(interest=topics,name=name)
        time.sleep(1)
        print(name,mail,topics)

@sched.scheduled_job("cron",day_of_week="mon-sun",hour=17)
def send_20():
    df = pandas.read_excel(file)
    for name, mail, topics in zip(set(df["name"]), set(df["email"]), set(df["interest"])):

        mailing=MailSender(mail)
        mailing.send_message(interest=topics,name=name)
        time.sleep(1)
        print(name,mail,topics)

# #This was just for testing purposes
# @sched.scheduled_job("cron",day_of_week="wed",hour=8,minute=55)
# def check():
#     df = pandas.read_excel(file)
#     for name, mail, topics in zip(set(df["name"]), set(df["email"]), set(df["interest"])):
#
#         print("I'm Alive \n")
#         print(name,mail,topics)


# #Testing as well
# @sched.scheduled_job("interval",seconds=10)
# def check():
#     df = pandas.read_excel(file)
#     for name, mail, topics in zip(df["name"], df["email"], df["interest"]):
#
#         print("I'm Alive")
#         print(name,mail,topics)

sched.start()
