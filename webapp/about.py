import justpy as jp


class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        page_div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
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


jp.Route(About.path, About.serve)
jp.justpy()
