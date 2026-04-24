"""4/21 ~1:07-1:10 PM - first Person, __init__, __str__."""


class Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old."


if __name__ == "__main__":
    p1 = Person("Mickey", 100)
    print(p1)
    print(p1.name)
