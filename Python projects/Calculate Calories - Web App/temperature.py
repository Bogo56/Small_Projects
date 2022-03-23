from selectorlib import Extractor
import requests
from selectorlib import Extractor

extractor=Extractor.from_yaml_file("selector.yaml")
url="https://www.timeanddate.com/weather/{}/{}"
headers = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}




class Temperature:

    def __init__(self,city,country):
        self.city=city.replace(" ","-").lower()
        self.country=country.replace(" ","-").lower()

    def get_temp(self):
            link= url.format(self.country,self.city)
            res=requests.get(link,headers=headers)
            temp=extractor.extract(res.text)["temp"].strip('\xa0°C')
            return float(temp)


if __name__=="__main__":
    test=Temperature("VaRnA","Bulgaria").get_temp()

