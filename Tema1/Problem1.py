# import numpy as np
# from decimal import *
import random
from tkinter import *


def compute_u():
    '''

    :return: tuple (m, u) that satisfy condition 1.0 + u != 1.0 where u = 1/10**m
    '''
    m = 1
    u = 0.1
    found = True
    while 1.0 + u != 1.0:
        u = u / 10.0
        m += 1
    return (m,u)

if __name__ == "__main__":
    m, u = compute_u()
    root = Tk()
    root.wm_title('Problem 1')
    # Code to add widgets will go here...
    Label(root, text='m = {number}'.format(number=m - 1), justify = LEFT).grid(row=0, column = 0)
    Label(root, text='u = {number}'.format(number=u), justify = LEFT).grid(row=1, column = 0)
    root.mainloop()
