import justpy as jp


@jp.SetRoute("/")   # creates a route with a decorator
def homepage():
    wp = jp.WebPage()   # instantiate a WebPage instance

    # 'classes' -
    # add styling as tailwind css (need space after split classes lines)

    # create div for page level styling
    page_div = jp.Div(a=wp, classes="bg-gray-200 h-screen")  # h = height

    # organise elements into grid
    div1 = jp.Div(a=page_div, classes="grid grid-cols-3 gap-4 p-4")  # p = padding, m = margin

    # assign form inputs to variables
    input_1 = jp.Input(a=div1, placeholder="Enter first value", classes="form-input")
    input_2 = jp.Input(a=div1, placeholder="Enter second value", classes="form-input")

    # assign an output variable to a div + receive d.text from button
    d_output = jp.Div(a=div1, text="Result goes here...", classes="text-gray-600")

    jp.Div(a=div1, text="Just another div...", classes="text-gray-600")
    jp.Div(a=div1, text="Yet another div...", classes="text-gray-600")


    # organise second layer of elements into a grid
    div2 = jp.Div(a=page_div, classes="grid grid-cols-2 gap-4")

    # Add a calculate button to div2
    # Set the click event handler to the sum_up functio
    # Pass inputs 1 + 2 from form to the button
    jp.Button(a=div2, text="Calculate", click=sum_up, input_1=input_1, input_2=input_2,
              classes="border border-blue-500 m-2 py-1 px-4 rounded "
              "text-blue-600 hover:bg-red-500 hover:text-white",
              d=d_output)  # passes result from sum_up to d_output
    jp.Div(a=div2, text="I am a cool interactive div!", classes="text-gray-600")
    return wp


def sum_up(widget, msg):
    # Event handler for button click: justpy passes the clicked widget
    # and an event message when sum_up called
    sum_result = float(widget.input_1.value) + float(widget.input_2.value)
    # pass the result back to the button
    widget.d.text = sum_result


# jp.Route("/", homepage)  # creates a route with a function


jp.justpy()
