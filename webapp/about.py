import justpy as jp
from webapp import layout

class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        page_div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=page_div,text="This is the About page!",
               classes="text-4xl ,m-2")
        jp.Div(a=page_div, text="""
            There once was a ChatGPT named "Four",
            Whose knowledge did endlessly pour,
            It answered with flair,
            And showed it did care,
            As users kept coming for more!
        """, classes="text-lg")
        return wp


