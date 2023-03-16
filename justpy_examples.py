import justpy as jp


@jp.SetRoute("/")   # creates a route with a decorator
def homepage():
    wp = jp.WebPage()   # instantiate a WebPage instance

    # 'classes' -
    # add styling as tailwind css (need space after split classes lines)

    # create div for page level styling
    page_div = jp.Div(a=wp, classes="bg-gray-200 h-screen")  # h = height

    # organise elements into grid
    div1 = jp.Div(a=page_div, classes="grid grid-cols-3 gap-4 p-4")
    jp.Input(a=div1, placeholder="Enter first value",
             classes="form-input")
    jp.Input(a=div1, placeholder="Enter second value",
             classes="form-input")
    jp.Div(a=div1, text="Result goes here...", classes="text-gray-600")
    jp.Div(a=div1, text="Just another div...", classes="text-gray-600")
    jp.Div(a=div1, text="Yet another div...", classes="text-gray-600")

    div2 = jp.Div(a=page_div, classes="grid grid-cols-2 gap-4")
    jp.Button(a=div2, text="Calculate",
              classes="border border-blue-500 m-2 py-1 px-4 rounded "
              "text-blue-600 hover:bg-red-500 hover:text-white")  # m = margin, p = padding
    jp.Div(a=div2, text="I am a cool interactive div!", classes="text-gray-600")
    return wp

# jp.Route("/", homepage)  # creates a route with a function


jp.justpy()
