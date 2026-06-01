#!/usr/bin/python3
a = 1
b = 2
def add():
    return a + b
if __name__ == "__main__":
    print("{a} + {b} = {add()}".format(a=a, b=b, add=add))
