from email.mime.text import MIMEText
import smtplib

def send_email(email,salary,avg_salary,respondents):
    from_email="actioncoachbot@gmail.com"
    password="xyvyxlthiwjtsaab"
    to_email=email

    subject="Salary Survey"
    message="Hey there, your salary is <strong>{}<strong>, the average Salary for the industry is <strong>{}<strong> based on survey upon {} respondents".format(salary,avg_salary,respondents)

    msg=MIMEText(message, "html")
    msg["Subject"]=subject
    msg["To"]=to_email
    msg["From"]=from_email

    gmail=smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,password)
    gmail.send_message(msg)