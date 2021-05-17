import random
from pathlib import Path
import math


def get_circle_length(r):
    return math.pi * r * 2

def add(a,b):
    return a + b

def get_current_dir():
    print(Path.cwd())

def get_random_digit():
    return random.randint(0, 100)

def main():
    res_dig = add(10, 20)
    res_str = add("Hello ", "world")
    print(res_dig, res_str)

    a = get_current_dir()
    b = get_random_digit()
    print(a, b)

    print(get_circle_length(22))

if __name__ == '__main__':
    main()
