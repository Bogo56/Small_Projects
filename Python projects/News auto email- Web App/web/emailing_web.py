import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from news_web import NewsFeed
from security_web import decPASS



#The class for sending the mail
class MailSender:

    sender_email="actioncoachbot@gmail.com"
    sender_pass=decPASS

    def __init__(self,receiver_email):
        self.receiver_email=receiver_email

        self.message=MIMEMultipart("alternative")
        self.message["Subject"]="Today's Hot News"
        self.message["From"]=self.sender_email
        self.message["To"]=self.receiver_email

    def send_message(self,interest,date=NewsFeed.date_today,name=""):

        newsfeed=NewsFeed(interest,date=date)
        newsfeed_news=newsfeed.get_news()
        news=""

###Sending no more than 10 articles
        if len(newsfeed_news["articles"])>10:
            for article in newsfeed_news["articles"][:10]:
                news = news + "{}\n\n{}\n{}\n\n\n".format(article["title"], article["description"], article["url"])
        else:
            for article in newsfeed_news["articles"]:
                news = news + "{}\n\n{}\n{}\n\n\n".format(article["title"], article["description"], article["url"])

###Creating two versions of meil - text version only and html. Text version is a backup option, when the mail client cant read the HTML version.
        text=f'''
        Hey {name},
        
        So this is what's cookin today {NewsFeed.date_today}!
        
        
        {news}
        
        
        Sincerely yours,
        
        Your Favourite News Chatbot
        
        '''
#Calling the render method which creates the html template
        html=self.render_html_body(newsfeed_news["articles"],name=name)

        part1=MIMEText(text,"plain")
        part2=MIMEText(html,"html")

        self.message.attach(part1)
        self.message.attach(part2)

        context=ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
            server.login(self.sender_email,self.sender_pass)
            server.sendmail(self.sender_email,self.receiver_email,self.message.as_string())

###The method for creating an HTML version of the mail(looks more fancy)
    def render_html_body(self,news,name=""):

        news_feed=""

        if len(news)>10:
            for item in news[:10]:
                news_feed=news_feed + f"""<h3>{item['title']}</h3>
                                          <img src={item['urlToImage']} width='500' height='300'>
                                            <p>{item['description']}<br>
                                            <a href="{item['url']}">Read More</a><br><br><br>
                                           </p>"""
        else:
            for item in news:
                news_feed=news_feed + f"""<h3>{item['title']}</h3>
                                            <p>{item['description']}<br>
                                            <a href="{item['url']}">Read More</a><br><br>
                                           </p>"""

        html_template = f"""
                <html>
                    <body>
                        <h2>Hey {name},<br>
                            So this is what's cookin today {NewsFeed.date_today}!<br><br><br>
                        </h2>
                        <div>
                        {news_feed}
                        </div>
                        <h4>Sincerely yours,<br><br>
                            Your Favourite News Chatbot<\h4>
                    </body>
                </html>
                """

        return html_template



###All of that code is run in just 2 lines - Pure ART
if __name__=="__main__":
    mailing=MailSender("mussashi50@gmail.com")
    mailing.send_message("bitcoin,crypto,etherium")
    print("Mail Send")



