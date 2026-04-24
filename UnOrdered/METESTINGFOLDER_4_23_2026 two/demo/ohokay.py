class MyClass:
    def __init__(self):
        self.x = 0
        self.y = 0

    def add(self):
        return self.x + self.y
    def add1(self,  some):
        return some.x + some.y
a=MyClass()
a.x = 5
a.y = 10
print(a.add())  # Output: 15