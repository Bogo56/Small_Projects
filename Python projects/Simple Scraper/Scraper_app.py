import requests
import bs4
import pandas 
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_file("Interface.kv")






class MainScreen(Screen):

    def property_link(self,url):
        r=requests.get(url)
        res=r.content
        


    
        soup=bs4.BeautifulSoup(res,"html.parser")


        listings=soup.select(".property-card-primary-info")


        price=soup.select(".listing-price")
        adress=soup.find_all(attrs={"class":"property-address"})
        city=soup.select(".property-city")
        broker=soup.select('.property-card-attribution')
        links=soup.select(".listing-price[href]")


        listings={"Property_Price":[],"Adress":[],"City":[],"Broker":[],"Link_to_listing":[]}

        for a,b,c,d,e in zip(price,adress,city,broker,links):
            listings["Property_Price"].append(a.text.strip())
            listings["Adress"].append(b.text.strip())
            listings["City"].append(c.text.strip())
            listings["Broker"].append(d.text.strip())
            listings["Link_to_listing"].append("http://"+"www.century21.com"+ e["href"])

        str1=""
        n=0
        for a,b,c,d,e in zip(listings["City"],listings["Adress"],listings["Property_Price"],listings["Broker"],listings["Link_to_listing"]):
            n+=1
            str1=str1 +f"{n}. {a}, {b}, {c}, {d} \n \n"
            

        self.ids.listings.text=str1


class MainApp(App):
    def build(self):
        return MainScreen()


if __name__=="__main__":
    MainApp().run()