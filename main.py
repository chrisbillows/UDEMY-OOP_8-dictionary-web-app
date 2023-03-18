import justpy as jp
import inspect

from webapp import page
from webapp.about import About
from webapp.dictionary import Dictionary
from webapp.home import Home

# DYNAMIC CREATION OF NEW ROUTES

imports = list(globals().values())

# globals() returns a dictionary representing the current global symbol table - contains all global variables,
# functions, and classes available in the current scope.
#
# In other words, it holds the global namespace's content, including any imported modules
# and their respective objects, as well as any user-defined global variables and functions
#
# Throw to a list as the for loop adds variables changing the dictionary as it's used

for obj in imports:
    if inspect.isclass(obj):
        if hasattr(obj, "path") and issubclass(obj, page.Page):
            jp.Route(obj.path, obj.serve)

    # filters out non-classes
    # filters only objects with a path attribute
    #  i.e. our page classes
    # Add hasattr filter - so page.Page class not filtered


# MANUAL CREATION OF NEW ROUTES

# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)
# jp.Route(Home.path, Home.serve)

jp.justpy()
