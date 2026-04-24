"""4/21 ~1:25-1:29 PM - Calculator class."""


class Calculator:
    def add(self, numbers):
        return sum(numbers)

    def subtract(self, a, b):
        return a - b


if __name__ == "__main__":
    c = Calculator()
    print(c.add([1, 2]))
    print(c.add([1, 2, 3, 4]))
    print(c.subtract(10, 4))
