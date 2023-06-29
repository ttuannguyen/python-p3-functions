#!/usr/bin/env python3

def greet_programmer():
    #print("Hello, programmer!")
    return "Hello, programmer!"

# print(greet_programmer())

def greet(name):
    return f"Hello, {name}!"

# print(greet("Tuan"))

def greet_with_default(name="programmer"):
    return f"Hello, {name}!"

# print(greet_with_default())


def add(num1, num2):
    return num1 + num2

# print(add(4,8))

def halve(number):
    return number / 2

print(halve(32))

