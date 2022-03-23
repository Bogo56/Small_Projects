import justpy as jp

class PageLayouts(jp.QLayout):

    def __init__(self,view="hHh lpR lFf",**kwargs):
        super().__init__(view=view,**kwargs)

##HEADER
        header = jp.QHeader(a=self, elevated=True)
        toolbar = jp.QToolbar(a=header)
        drawer = jp.QDrawer(a=self, v_mode="left", show_if_above=True,
                            bordered=True, content_class="bg-primary text-white",
                            classes="shadow-2 rounded-borders")
        t_but1 = jp.QButton(a=toolbar, flat=True, round=True, dense=True, icon='menu', classes="q-mr-sm",
                            click=self.drawer_on, drawers=drawer)
        avatar = jp.QAvatar(a=toolbar, size="62px")
        avatar_image = jp.QImg(a=avatar,
                               src="https://www.pngfind.com/pngs/m/48-486774_png-file-book-icon-png-transparent-vector-png.png")
        toolbar_title = jp.QToolbarTitle(a=toolbar, text="Online Dictionary")
        t_bu2 = jp.QButton(a=toolbar, flat=True, round=True, dense=True, icon="whatshot")
##HEADER END
##DRAWER
        scroll_area = jp.QScrollArea(a=drawer, classes="fit")
        q_list = jp.QList(a=scroll_area, classes="q-pa-md")
        q_item1 = jp.QItem(a=q_list, clickable=True, v_ripple=True)
        link1 = jp.A(a=q_item1, href="/about", text='ABOUT', classes="text-h4")
        q_item2 = jp.QItem(a=q_list, clickable=True, v_ripple=True)
        link1 = jp.A(a=q_item2, href="/dictionary", text='DICTIONARY', classes="text-h4")
        q_item3 = jp.QItem(a=q_list, clickable=True, v_ripple=True)
        link1 = jp.A(a=q_item3, href="/", text='HOME', classes="text-h4")

    @staticmethod
    def drawer_on(widget, msg):
        if widget.drawers.value:
            widget.drawers.value = False
        else:
            widget.drawers.value = True