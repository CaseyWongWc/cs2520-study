"""4/21 ~1:11-1:16 PM - private attrs, get/set methods.

Shown in class:
  1. self._name  (convention)
  2. self.__name (name-mangled to _Person__name)
  3. get_name()/set_name() as the proper accessors
"""


class Person:
    def __init__(self, name="Unknown", age=0):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age


if __name__ == "__main__":
    p1 = Person("Mickey", 100)
    print(p1.get_name())
    p1.set_name("Mouse")
    print(p1.get_name())
