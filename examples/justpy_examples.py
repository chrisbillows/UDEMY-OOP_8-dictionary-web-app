import justpy as jp


@jp.SetRoute("/")   # creates a route with a decorator
def homepage():
    wp = jp.QuasarPage(tailwind=True)   # instantiate a QuasarPage (Vue.js) instance for increased functionality

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

    # organise second layer of elements into a grid
    div2 = jp.Div(a=page_div, classes="grid grid-cols-2 gap-4")

    # Add a calculate button to div2
    # Set the click event handler to the sum_up functio
    # Pass inputs 1 + 2 from form to the button
    # Updated to a Quasar button + Quasar properties
    jp.QBtn(a=div2, round=True, color="primary", icon="shopping_cart",  text="Calculate",
            click=sum_up, input_1=input_1, input_2=input_2, d=d_output)
    #  passes result from sum_up to d_output
    jp.Div(a=div2, text="I am a cool interactive div!",
           mouseenter=mouse_enter, mouseleave=mouse_leave,
           classes="hover:bg-red-500")
    return wp


def sum_up(widget, msg):
    # Event handler for button click: justpy passes the clicked widget
    # and an event message when sum_up called
    sum_result = float(widget.input_1.value) + float(widget.input_2.value)
    # pass the result back to the button
    widget.d.text = sum_result


def mouse_enter(widget, msg):
    # event handlers to change div text
    widget.text = "A mouse entered the house!"


def mouse_leave(widget, msg):
    widget.text = "The mouse left!"

# jp.Route("/", homepage)  # creates a route with a function


jp.justpy()
