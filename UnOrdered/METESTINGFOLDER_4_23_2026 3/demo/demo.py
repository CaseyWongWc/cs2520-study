from test_input import setin
setin("Alice", "30")
from demo.person import Person
person = Person(input("Enter name: "), input("Enter age: "))
print(person.greet())
