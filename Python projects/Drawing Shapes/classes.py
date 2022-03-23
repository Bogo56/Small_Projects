from PIL import Image, ImageDraw


class Canvas:
    def __init__(self,size,background_color="white",):

        self.image = Image.new("RGB", size, background_color)
        self.size=size
        self.background_color=background_color
        self.name="Drawing_App.jpg"

    def open(self):
        Image.open(self.name)

    def save(self):
        self.image.save(self.name)


class Rect_Shape():

    def __init__(self,size,color="white"):
        self.size=size
        self.color=color

    def create(self,image_file):
        draw=ImageDraw.Draw(image_file)
        draw.rectangle((self.size),fill=self.color)



