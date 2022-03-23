from security_web import decKEY
import requests
from datetime import datetime

## This module is communicating with the NEWS API

##I wrote a security module which encrypts the password
## It was supposed to be used for the email password, but instead I did it for the API key - got distracted

class NewsFeed:


    key=decKEY
    base_url="http://newsapi.org/v2/everything?"
    date_today=datetime.now().strftime("%Y-%m-%d")

    def __init__(self,topic,language="en",date=date_today):
        self.topic=topic
        self.language=language
        self.date=date

        query=f"language={self.language}" \
              f"&sortBy=popularity" \
              f"&qInTitle={self.topic}" \
              f"&from={self.date}" \
              f"&apiKey={self.key}"

        self.final_url=self.base_url + query

    def get_news(self):
        res=requests.get(self.final_url)
        news=res.json()
        return news

### Using properties to define the value of the attribute
    @property
    def topic(self):
        return self._topic

    @topic.setter
    def topic(self,interest):
        self._topic=interest.replace(",","%20OR%20")



if __name__=="__main__":
    test_news=NewsFeed("bitcoin")
    test_news_news=test_news.get_news()
    check_prop=test_news.topic
    print(test_news_news["articles"][1]["title"])
