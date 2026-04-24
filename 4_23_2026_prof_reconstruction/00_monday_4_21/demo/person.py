"""4/21 ~1:32-1:36 PM - final Person, moved into demo/ package.

Fixes the in-class bug where is_adult was @staticmethod but used self.age.
Here it takes age as an explicit parameter.
"""


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

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age

    def show_info(self):
        print(f"{self._name} is an adult? {Person.is_adult(self._age)}")

    @staticmethod
    def is_adult(age):
        return age >= 18


if __name__ == "__main__":
    p1 = Person("Mickey", 10)
    p1.show_info()
    p1.age = 25
    p1.show_info()
