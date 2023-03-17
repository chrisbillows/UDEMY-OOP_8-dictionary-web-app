import justpy as jp

from webapp.about import About
from webapp.dictionary import Dictionary
from webapp.home import Home


jp.Route(About.path, About.serve)
jp.Route(Dictionary.path, Dictionary.serve)
jp.Route(Home.path, Home.serve)
jp.justpy()

