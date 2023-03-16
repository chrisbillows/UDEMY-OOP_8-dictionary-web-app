import justpy as jp


@jp.SetRoute("/")   # creates a route with a decorator
def homepage():
    wp = jp.WebPage()   # instantiate a WebPage instance

    # create div for page level styling
    page_div = jp.Div(a=wp, classes="bg-gray-200 h-screen")  # h = height

    # classes - add styling as tailwind css (need space after split classes lines)
    jp.Input(a=page_div, placeholder="Enter first value",
             classes="form-input")
    jp.Input(a=page_div, placeholder="Enter second value",
             classes="form-input")
    jp.Div(a=page_div, text="Result goes here...", classes="text-gray-600")
    jp.Button(a=page_div, text="Calculate",
              classes="border border-blue-500 m-2 py-1 px-4 rounded "
              "text-blue-600 hover:bg-red-500 hover:text-white")  # m = margin, p = padding
    return wp

# jp.Route("/", homepage)  # creates a route with a function


jp.justpy()
