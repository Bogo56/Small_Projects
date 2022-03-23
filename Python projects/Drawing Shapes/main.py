from classes import Canvas, Rect_Shape


def square(canvas,shape_color,fig_x,fig_y):
    sqr_size = int(input("What's the square side lenght?  "))
    sqr_size=(fig_x,fig_y,fig_x+sqr_size,fig_y+sqr_size)
    square = Rect_Shape(sqr_size, color=shape_color)
    square.create(canvas.image)

def rectangle(canvas,shape_color,fig_x,fig_y):
    rect_height = int(input("What's the height of the Rectangle?  "))
    rect_width = int(input("What's the width of the Rectangle?  "))
    rect_size =(fig_x,fig_y,fig_x+rect_width,fig_y+rect_height)
    rectangle = Rect_Shape(rect_size, color=shape_color)
    rectangle.create(canvas.image)


canvas=Canvas((800,800))

while True:

    figure = (input("What would you like to draw?(Square,Rectangle) ")).lower()
    while figure not in (("square","rectangle")):
        figure =input("Plese choose Square or Rectangle:  ").lower()

    shape_color = input("What color should the shape be?(green,blue,orange,yellow,purple):  ")

    fig_x = int(input("What's the X coordinate of the shape?  "))
    fig_y = int(input("What's the Y coordinate of the shape?  "))

    if figure=="square":
        square(canvas, shape_color, fig_x, fig_y)
    elif figure=="rectangle":
        rectangle(canvas, shape_color, fig_x, fig_y)

    wanna_quit=input("Type Q to quit, or press Enter to continue: ").lower()
    if wanna_quit =="q":
        break



canvas.save()
print("Drawing completed")



