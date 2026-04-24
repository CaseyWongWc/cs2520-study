class Person:
    def __init__(self, name="Unknown", age=1):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

p1 = Person("Mickey", 100)
print(p1.get_name())
p1.set_name("Mouse")
print(p1.get_name())
