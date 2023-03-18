import justpy as jp
from webapp import layout
from webapp import page


class Home(page.Page):
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        page_div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=page_div,text="This is the Home page!",
               classes="text-4xl ,m-2")
        jp.Div(a=page_div, text="""
Once upon a time in a charming village, there lived a curious squirrel named Whiskers. Whiskers was always exploring the dense woods, scampering up and down the tall trees, searching for the tastiest acorns he could find. His enthusiasm for adventure was contagious, and he had many friends among the woodland creatures.

In the heart of the forest, a wise old owl named Hoot perched high on the branches of an ancient oak tree. Hoot was known far and wide for his intelligence and insight. Animals from all corners of the woods would come to seek his advice and guidance on matters both big and small. Hoot was always happy to share his wisdom with those in need.

One day, a young rabbit named Daisy approached Hoot with a problem. She had been trying to grow a beautiful flower garden but was struggling to keep her plants healthy and vibrant. Hoot listened carefully to Daisy's concerns and suggested she consult with a friendly ladybug named Rosie, who had a knack for tending to plants and flowers.

Rosie was delighted to help Daisy with her garden, and together they worked tirelessly to nurture the delicate blooms. They watered the flowers, removed weeds, and protected the plants from hungry insects. With Rosie's guidance and Daisy's dedication, the garden soon flourished, bursting with color and fragrance.

The garden became a popular gathering place for the woodland creatures, who marveled at the stunning flowers and enjoyed the peaceful atmosphere. Whiskers, Hoot, and their friends spent many happy hours there, basking in the beauty of the blossoms and the warmth of their friendships. As the seasons changed, the garden continued to thrive, a testament to the power of collaboration and the magic of the forest.

And so, the enchanting village and its inhabitants carried on, living in harmony with nature and cherishing the connections they shared. Through love, cooperation, and understanding, they created a world full of joy and wonder, where every creature had a place to call home.    
        """, classes="text-lg")
        return wp
