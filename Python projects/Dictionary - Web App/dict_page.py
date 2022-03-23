from layout import PageLayouts
import justpy as jp
import pandas
from about_page import AboutPage

df=pandas.read_csv("data.csv")
#We want to print the full Strings and not ...
pandas.set_option("display.max_colwidth",None)


class HomePage:
    route="/"

    @classmethod
    def home_page(cls):
        wp=jp.QuasarPage(tailwind=True)
        div_main=jp.QDiv(a=wp,classes="q-pa-md")
        div_one=jp.QDiv(a=div_main)
## CReated The Header and Side Menu as a separate class to save some coding and reuse it
        layout=PageLayouts(a=div_one,view="hHh lpR lFf",container=True,
                                  style="height:675px",classes="shadow-2 rounded-borders",
                                  overflow="hidden")
### BODY
        page_cont=jp.QPageContainer(a=layout,classes="q-pa-md")
        page=jp.QPage(a=page_cont,classes="g-gutter-md")
        page_row=jp.QDiv(a=page,classes="row justify-around q-mt-xl q-pt-md q-ml-lg ")
### COLUMN 1
        page_col1 = jp.QDiv(a=page_row, classes="column items-center ", style="max-width:200px")
###COLUMN 2
        page_col2=jp.QDiv(a=page_row,classes="column content-center", style="max-width:200px")
        scroll=jp.QScrollArea(a=page_col2,style="height:300px; width:500px;", classess="bg-black rounded-borders fixed-center")
        paragraph=jp.QDiv(a=scroll,text="Definition will be displayed here",classes=" text-grey-6 text-body1")

### This belongs to Column 1 but because we want to refrence paragraph variable that is after Column 1 we have to put it here after Column 2
        inputs = jp.QInput(a=page_col1, rounded=True, outlined=True, v_model="text", style="width:300px",
                          label="Type word here")
        p_but1 = jp.QButton(a=page_col1, rounded=True, color="teal", glossy=True, label="Translate",
                            style="max-height:50px;width:250px;", classes="q-mt-xl", mouseenter=cls.mouse_in,
                            mouseleave=cls.mouse_out,scroll_field=paragraph,typing=inputs,click=cls.click_button)
        but1_icon = jp.QIcon(a=p_but1, left=True, name="map", size="3em")

        return wp


## We use static methods because using them as classmethods doesn't work. The way this Framework works is that it doesn't
    # instantiate the Class, so we use classmethod,because 'self' needs an instance. But here if we use cls as a first argument for the class method
    # it does not work also, JustPy expects a widget as first argument and not the cls, so this is why we use staticmethods##
    @staticmethod
    def mouse_in(widget,msg):
        widget.color="light-blue"


    @staticmethod
    def mouse_out(widget,msg):
        widget.color="teal"


    @staticmethod
    def click_button(widget,msg):
        term=widget.typing.value
        definition=df[df["word"] == term]["definition"]
        if definition.size==0:
            widget.scroll_field.text = "We can't find that word in our database"
        else:
            widget.scroll_field.text = definition.to_string(index=False)

        widget.scroll_field.classes="text-black text-body1"








if __name__=="__main__":
    jp.Route(AboutPage.route,AboutPage.about_page)

    jp.justpy(HomePage.home_page)


