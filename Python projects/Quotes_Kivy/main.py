from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
import json
from datetime import datetime
import random
import os

##WE LOAD THE KV FILE AND SO THE CLASSES COMMUNICATE BETWEEN THEMSELVES, ELSE I WOULD HAVE TO WRITE
# MORE CONFUSING PYTHON KV OBJECTS 

Builder.load_file("design.kv")


class LoginScreen(Screen):

    def sign_up(self):
        #Switching between Screens
        self.manager.current="sign_up_screen"
    
    def login(self,user,password):

        with open("users_test.json") as file:
            users=json.load(file)

            if user in users:
                if users[user]["username"]==password:
                ## LOADING THE LOGED SCREEN BY REFRENCING IT'S NAME IN THE <RootWidget>
                    self.manager.current="loged_screen"
                else:
                    Popup().open()
            else:
                pass
        
    


class LogedScreen(Screen):

    def log_out(self):
        self.manager.current="login_screen"
        self.manager.transition.direction="right"

    def show_quote(self,feel=""):
        feel=feel.lower()
    
        for n in os.listdir("quotes"):
                if n.startswith(feel):
                        with open(f"quotes/{n}",encoding="utf8") as file:
                            lst1=file.read().splitlines()
                            res=random.choice(lst1)
                            break
                else:
                    res="Try another keyword"
                
            

                
            
## WE ACCESS THE CLASS WITH self THEN USE THE LABEL ID "quotes" IN THAT CLASS(<LogedScreen> in .kv file)
## THEN CHOOSE text ATTRIBUTE OF THE LABEL OBJECT AND ASSIGN IT                   
        self.ids.quotes.text=res
                



class RootWidget(ScreenManager):
    pass


class SignUpScreen(Screen):
    def add_user(self,user,password):

        with open("users_test.json") as file:
            users=json.load(file)
            
        users[user]={"username":user,"password":password,"created": datetime.now().strftime("%Y-%m-%d")}
        
        with open ("users_test.json","w") as file:
            json.dump(users,file)

        self.manager.current="sign_up_success"
        
    def home(self):
        
        self.manager.transition.direction="right"
        self.manager.current="login_screen"
        
            
class SignUpScreenSuccess(Screen):

    def home(self):
        
        self.manager.transition.direction="right"
        self.manager.current="login_screen"
            
class PopUp(Popup):
    pass
    


class MainApp(App):
    def build (self):
        return RootWidget()


if __name__=="__main__":
    MainApp().run()