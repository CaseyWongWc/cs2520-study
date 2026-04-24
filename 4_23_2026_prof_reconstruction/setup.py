"""Bootstrap: materializes the CS 2520 4/21 + 4/23 reconstruction.
Run from inside 4_23_2026_prof_reconstruction/ :  python setup.py
Safe to re-run (overwrites)."""
import os

F = {}

F["README.md"] = """# CS 2520 - Professor's Codespace Reconstruction

**Dates covered:** Monday 4/21/2026 + Thursday 4/23/2026
**Topics:** Python Properties -> Modules/Packages -> File I/O

## Purpose
Reconstructs the in-class demo/ codespace from 4/21 and 4/23 lectures.
Assembled from ImageDrop photo OCR + Notion class notes.

## Status of sources
- 4/21 (Monday): First ~7 min missed (late arrival). Reconstruction starts
  at 1:07 PM when the prof said "create a file called person."
- 4/23 (Thursday): Reconstructed from Notion (file I/O focus).

## How to run
    python 00_monday_4_21/01_person_basic.py
    python 00_monday_4_21/03_person_property.py
    cd 00_monday_4_21 && python demo/demo.py
    python 01_thursday_4_23/01_file_write.py
"""

F["00_monday_4_21/01_person_basic.py"] = '''"""4/21 ~1:07-1:10 PM - first Person, __init__, __str__."""


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
'''

F["00_monday_4_21/02_person_private.py"] = '''"""4/21 ~1:11-1:16 PM - private attrs, get/set methods.

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
'''

F["00_monday_4_21/03_person_property.py"] = '''"""4/21 ~1:16-1:20 PM - @property and @name.setter."""


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
'''

F["00_monday_4_21/04_modules_stdlib.py"] = '''"""4/21 ~1:41-1:48 PM - import / import as / from import."""
import math, random, os
print("math.sqrt(16) =", math.sqrt(16))
print("math.pi       =", math.pi)
print("random.randint(1,10) =", random.randint(1, 10))
print("os.getcwd()   =", os.getcwd())

import math as m
print("m.sqrt(25)    =", m.sqrt(25))

from math import sqrt, pi, pow
print("sqrt(36)      =", sqrt(36))
print("pow(2, 3)     =", pow(2, 3))

from datetime import datetime as dt
print("today         =", dt.now())
'''

F["00_monday_4_21/module_a.py"] = '''"""4/21 helper module for cross-file import demo."""


def echo(name):
    print(name)
'''

F["00_monday_4_21/module_b.py"] = '''"""4/21 imports module_a and calls its function.
Run from 00_monday_4_21/:   python module_b.py
"""
import module_a
module_a.echo("Go Broncooo!")
'''

F["00_monday_4_21/demo/__init__.py"] = '''"""Marks demo/ as a Python package."""
'''

F["00_monday_4_21/demo/person.py"] = '''"""4/21 ~1:32-1:36 PM - final Person, moved into demo/ package.

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
'''

F["00_monday_4_21/demo/calculator.py"] = '''"""4/21 ~1:25-1:29 PM - Calculator class."""


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
'''

F["00_monday_4_21/demo/demo.py"] = '''"""4/21 driver inside demo/ package.
Run from 00_monday_4_21/ :   python demo/demo.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from person import Person
from calculator import Calculator


def main():
    p = Person("Mickey", 25)
    p.show_info()
    c = Calculator()
    print("1 + 2 + 3 =", c.add([1, 2, 3]))


if __name__ == "__main__":
    main()
'''

F["01_thursday_4_23/01_file_write.py"] = '''"""4/23 - writing to a file.
Three steps: open() -> write() -> close().
Mode 'w' creates or overwrites.
"""
outfile = open("customers.txt", "w")
outfile.write("Bruno\\n")
outfile.write("Alice\\n")
outfile.write("Chen\\n")
outfile.close()

print("Wrote 3 lines to customers.txt")
print("---- file contents ----")
with open("customers.txt") as f:
    print(f.read())
'''

F["01_thursday_4_23/02_file_append.py"] = '''"""4/23 - appending to a file.
Mode 'a' keeps existing content. Run 01_file_write.py first.
"""
outfile = open("customers.txt", "a")
outfile.write("Sam\\n")
outfile.write("Dana\\n")
outfile.close()

print("Appended 2 lines.")
with open("customers.txt") as f:
    print(f.read())
'''

F["01_thursday_4_23/03_numeric_data.py"] = '''"""4/23 - handling numeric data with files.
Files store STRINGS. Convert both directions:
  write:  str(num)
  read:   int(s) / float(s)
"""
prices = [9.99, 14.50, 3.25]
out = open("prices.txt", "w")
for p in prices:
    out.write(str(p) + "\\n")
out.close()

total = 0.0
with open("prices.txt") as f:
    for line in f:
        total += float(line.strip())
print("Total: $", total)
'''

F["01_thursday_4_23/04_raw_strings_escapes.py"] = r'''"""4/23 - raw strings and escape characters.
Windows paths break because \ is an escape char. Three fixes:
"""
path_raw = r"C:\Users\Bronco\Documents\Python\notes.txt"
print("raw   :", path_raw)

path_esc = "C:\\Users\\Bronco\\Documents\\Python\\notes.txt"
print("esc   :", path_esc)

path_fwd = "C:/Users/Bronco/Documents/Python/notes.txt"
print("fwd   :", path_fwd)

print("\nCommon escapes:")
print("tab\there")
print("newline:\nhere")
print("quote: \"double\" and 'single'")
print("backslash: \\")
'''

F["01_thursday_4_23/zybooks_11_8_artwork.py"] = '''"""4/23 - zyBooks 11.8 LAB: Artwork label (modules).

Standard inputs (newline-separated):
    Pablo Picasso
    1881
    1973
    Three Musicians
    1921

Expected output:
    Artist: Pablo Picasso (1881 to 1973)
    Title: Three Musicians, 1921
"""


class Artist:
    def __init__(self, name="unknown", birth_year=-1, death_year=-1):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year

    def print_info(self):
        b = "unknown" if self.birth_year == -1 else str(self.birth_year)
        if self.birth_year == -1:
            d = "unknown"
        elif self.death_year == -1:
            d = "present"
        else:
            d = str(self.death_year)
        print(f"Artist: {self.name} ({b} to {d})")


class Artwork:
    def __init__(self, title="unknown", year_created=-1, artist=None):
        self.title = title
        self.year_created = year_created
        self.artist = artist if artist else Artist()

    def print_info(self):
        self.artist.print_info()
        print(f"Title: {self.title}, {self.year_created}")


if __name__ == "__main__":
    name = input()
    by = int(input())
    dy = int(input())
    title = input()
    yc = int(input())
    a = Artist(name, by, dy)
    w = Artwork(title, yc, a)
    w.print_info()
'''

F["01_thursday_4_23/zybooks_11_9_guess.py"] = '''"""4/23 - zyBooks 11.9: Guess the random number.
Uses random.seed() for reproducibility, then randint(1,100).
"""
import random

random.seed(900)
target = random.randint(1, 100)

while True:
    g = int(input("Guess (1-100): "))
    if g < target:
        print("Too low")
    elif g > target:
        print("Too high")
    else:
        print("You got it!")
        break
'''

# --- materialize ---
for path, content in F.items():
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)

print("\nDone. Try: python 00_monday_4_21/demo/demo.py")