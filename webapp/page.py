from abc import ABC, abstractmethod


class Page(ABC):
    @abstractmethod
    def serve(self):
        pass


# creates an abstract class - a class that can't be instantiated
# this is used by the dynamic route creation to filter page classes from globals
