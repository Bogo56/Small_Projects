from kivy.config import Config
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from filestack import Client
import webbrowser,pyperclip


###-DEBUGGING-###

#from kivy.logger import Logger
#import logging
#Logger.setLevel(logging.TRACE)

####################

#Connecting to filestack-python trough our API
client=Client("ASvpijdoRkeOZCDfbtG6Qz")

Builder.load_file("front.kv")

#Adjusting window size
Config.set('graphics', 'resizable', '0')
Config.set("graphics", "width","500")
Config.set("graphics","height","700")


class CameraScreen(Screen):
    def turn_on(self):
        toggle=self.ids.toggler
        camera=self.ids.camera

        if toggle.state=="down":
            camera.play=True
            toggle.text="Stop"
            camera.opacity=1
        if toggle.state=="normal":
            camera.play=False
            toggle.text="Start"
            camera.opacity=0

    def capture(self):
        camera=self.ids.camera

        if camera.play==True:
            print("Capture")
            camera.export_to_png("Kivy_Snap.png")
            self.manager.current="image_screen"


class ImageScreen(Screen):

    def create_link(self):
        global new_link
        new_link=client.upload(filepath="Kivy_Snap.png")
        return new_link.url
    
    def open(self):
        try:
            webbrowser.open(new_link.url,new=2)
        except:
            pass
    
    def copy(self):
        try:
            pyperclip.copy(new_link.url)
        except:
            pass
    

class ScreenManager(ScreenManager):
    pass

class MyApp(App):

    def build(self):
        return ScreenManager()



if __name__=="__main__":
    MyApp().run()