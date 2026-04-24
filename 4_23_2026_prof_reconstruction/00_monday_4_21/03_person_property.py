"""4/21 ~1:16-1:20 PM - @property and @name.setter."""


class Person:
    def __init__(self, name="Unknown", age=0):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


if __name__ == "__main__":
    p1 = Person("Mickey", 100)
    print(p1.name)
    p1.name = "Mouse"
    print(p1.name)
