import random
from Problem1 import compute_u
from tkinter import *


def check_associativity(u):
    found = False
    y = z = u
    left_sum = right_sum = left_pro = right_pro = 0
    while not found:
        x = random.uniform(0, 1)
        left_sum = (x + y) + z
        right_sum = x + (y + z)

        left_pro = (x * y) * z
        right_pro = x * (y * z)
        found = left_sum != right_sum and left_pro != right_pro

    msg = "Asociativitatea nu mai este justa pentru x ={x}".format(x=x)
    sum_msg = 'Suma:     {left} != {right}'.format(left=left_sum,
                                                    right=right_sum)

    pro_msg = 'Produs:  {left} != {right} '.format(left=left_pro,
                                                      right=right_pro)
    return msg,sum_msg, pro_msg
if __name__ == "__main__":
    m, u = compute_u()
    msg, sum_msg, pro_msg = check_associativity(u)

    root = Tk()
    root.wm_title("Problem 2")

    Label(root, text=msg, justify=LEFT).grid(row=0, column=0)
    Label(root, text=sum_msg, justify=LEFT).grid(row=1, column=0)
    Label(root, text=pro_msg, justify=LEFT).grid(row=2, column=0)

    root.mainloop()
