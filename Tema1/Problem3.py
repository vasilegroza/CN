import math
from tkinter import *
import random

c1 = 1 / math.factorial(3)
c2 = 1 / math.factorial(5)
c3 = 1 / math.factorial(7)
c4 = 1 / math.factorial(9)
c5 = 1 / math.factorial(11)
c6 = 1 / math.factorial(13)

pi = math.pi

rnd = random.uniform(-pi / 2, pi / 2)


def p1(x, mod=0):
    if mod == 0:
        return x - c1 * (x ** 3) + c2 * (x ** 5)
    else:
        y = x * x
        return x * (y * (y * c2 - c1) + 1)


def p2(x, mod=0, p1=0):
    if mod == 0:
        return x - c1 * (x ** 3) + c2 * (x ** 5) - c3 * (x ** 7)
    elif mod == 1:
        y = x * x
        return x * (y * (y * (c2 - y * c3) - c1) + 1)
    else:
        y = x * x
        z = y * y
        return p1 - c3 * y * z * x


def p3(x, mod=0, p2=0):
    if mod == 0:
        return x - c1 * (x ** 3) + c2 * (x ** 5) - c3 * (x ** 7) + c4 * (x ** 9)
    elif mod == 1:
        y = x * x
        return x * (y * (y * (y * (y * c4 - c3) + c2) - c1) + 1)
    else:
        y2 = x * x
        y4 = y2 * y2
        y8 = y4 * y4
        return p2 * y8 * x


def p4(x, mod=0):
    if mod == 0:
        return x - 0.166 * (x ** 3) + 0.00833 * (x ** 5) - c3 * (x ** 7) + c4 * (x ** 9)
    else:
        y = x * x
        return x * (y * (y * (y * (y * c4 - c3) + 0.00833) - 0.166) + 1)


def p5(x, mod=0, p3=0):
    if mod == 0:
        return x - c1 * (x ** 3) + c2 * (x ** 5) - c3 * (x ** 7) + c4 * (x ** 9) - c5 * (x ** 11)
    elif mod == 1:
        y = x * x
        return x * (y * (y * (y * (y * (c4 - y * c5) - c3) + c2) - c1) + 1)


def p6(x, mod=0, p5=0):
    if mod == 0:
        return x - c1 * (x ** 3) + c2 * (x ** 5) - c3 * (x ** 7) + c4 * (x ** 9) - c5 * (x ** 11) + c6 * (x ** 13)
    elif mod == 1:
        y = x * x
        return x * (y * (y * (y * (y * (y * (y * c6 - c5) + c4) - c3) + c2) - c1) + 1)

def p1_v1(x):
    return x - c1 * (x ** 3) + c2 * (x ** 5)
def p1_v2(x):
    y = x * x
    return x * (y * (y * c2 - c1) + 1)

def p2_v1(x):
    return x - c1 * (x ** 3) + c2 * (x ** 5) - c3 * (x ** 7)
def p2_v2(x):
    y = x * x
    return x * (y * (y * (c2 - y * c3) - c1) + 1)

def p3_v1(x):
    return x - c1 * (x ** 3) + c2 * (x ** 5) - c3 * (x ** 7) + c4 * (x ** 9)
def p3_v2(x):
    y = x * x
    return x * (y * (y * (y * (y * c4 - c3) + c2) - c1) + 1)


def p4_v1(x):
    return x - 0.166 * (x ** 3) + 0.00833 * (x ** 5) - c3 * (x ** 7) + c4 * (x ** 9)
def p4_v2(x):
    y = x * x
    return x * (y * (y * (y * (y * c4 - c3) + 0.00833) - 0.166) + 1)


def p5_v1(x):
    return x - c1 * (x ** 3) + c2 * (x ** 5) - c3 * (x ** 7) + c4 * (x ** 9) - c5 * (x ** 11)
def p5_v2(x):
    y = x * x
    return x * (y * (y * (y * (y * (c4 - y * c5) - c3) + c2) - c1) + 1)


def p6_v1(x):
    return x - c1 * (x ** 3) + c2 * (x ** 5) - c3 * (x ** 7) + c4 * (x ** 9) - c5 * (x ** 11) + c6 * (x ** 13)
def p6_v2(x):
    y = x * x
    return x * (y * (y * (y * (y * (y * (y * c6 - c5) + c4) - c3) + c2) - c1) + 1)

print(p6(rnd, 0))
print(p6(rnd, 1))
print(math.sin(rnd))

# root = Tk()
# Label(root, text="First").grid(row=0)
# Label(root, text="Second").grid(row=1)
#
# e1 = Entry(root)
# e2 = Entry(root)
#
# e1.grid(row=5, column=4)
# e2.grid(row=1, column=1)
# root.mainloop(  )
