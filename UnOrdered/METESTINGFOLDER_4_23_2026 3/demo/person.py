class Person:
    def __init__(self, name="Unknown", age=1):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name
