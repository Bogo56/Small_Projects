import justpy as jp
from layout import PageLayouts

class AboutPage():
    route="/about"

    @classmethod
    def about_page(cls):
        wp = jp.QuasarPage(tailwind=True)
        div_main = jp.QDiv(a=wp, classes="q-pa-md")
        div_one = jp.QDiv(a=div_main)
## CReated The Header and Side Menu as a separate class to save some coding and reuse it
        layout = PageLayouts(a=div_one, view="hHh lpR lFf", container=True,
                             style="height:675px", classes="shadow-2 rounded-borders",
                             overflow="hidden")

        page_cont = jp.QPageContainer(a=layout, classes="q-pa-md")
        page = jp.QPage(a=page_cont, classes="g-gutter-md")
        page_row = jp.QDiv(a=page, classes="row justify-center q-mt-xl q-pt-md q-ml-lg ")
        page_col1=jp.QDiv(a=page_row,classes="column content-center ",style="width:350px")
        logo=jp.QImg(a=page_col1,
                     src="https://forum.teachingbooks.net/wp-content/uploads/2020/01/tb_bookonly_logo_square_600px-e1578263807999.jpg")
        paragraph=jp.QDiv(a=page_col1,text="some Text goes Here"*55, classes="q-mt-lg")




        return wp



