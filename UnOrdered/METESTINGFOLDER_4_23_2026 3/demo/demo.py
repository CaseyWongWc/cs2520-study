"""4/21 driver inside demo/ package.
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
