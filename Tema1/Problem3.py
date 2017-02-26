import math
from tkinter import *
import random
import time


def running_time_function(function, *args):
    start_time = time.time()
    # print("Start Function...")
    # print(function.__name__)
    result = function(args[0], args[1])
    # print("Finish Function")
    running_time = time.time() - start_time
    # print("Running time is:{time}".format(time=nice_time(running_time * 1000)))
    return running_time, result


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


def compute_error(rnd_list, fnct):
    return sum([math.fabs(fnct(i) - math.sin(i)) for i in rnd_list])


def compute_all_errors(rnd_list, mode=0):
    if mode == 0:
        polinoms = [p1_v1, p2_v1, p3_v1, p4_v1, p5_v1, p6_v1]
    else:
        polinoms = [p1_v2, p2_v2, p3_v2, p4_v2, p5_v2, p6_v2]
    time_and_errors = [(running_time_function(compute_error, rnd_list, polinoms[nr]), nr + 1) for nr in range(6)]
    time_and_errors = sorted(time_and_errors, key=lambda el: el[0][1])

    return time_and_errors


def create_labels(in_results, start_row):
    for i in range(len(in_results)):
        result = in_results[i]
        print(result)
        l_in = Label(root, text="P{nr}(x) has error:   {err}   and we compute it in:   {t}".format(nr=result[1],
                                                                                                   err=result[0][1],
                                                                                                   t=result[0][0]))
        l_in.grid(row=i + start_row, sticky=W)


if __name__ == "__main__":

    c1 = 1 / math.factorial(3)
    c2 = 1 / math.factorial(5)
    c3 = 1 / math.factorial(7)
    c4 = 1 / math.factorial(9)
    c5 = 1 / math.factorial(11)
    c6 = 1 / math.factorial(13)
    pi = math.pi

    randomList = [random.uniform(-pi / 2, pi / 2) for _ in range(10000)]

    root = Tk()
    root.wm_title("Problem3")
    l = Label(root, text="Eroarea folosind implementarea standard:")
    l.config(font=("Courier", 14))
    l.grid(row=0, sticky=W)

    result1 = compute_all_errors(randomList, 0)
    create_labels(result1, 1)

    l = Label(root, text="Eroarea folosind implementarea optimizata:")
    l.config(font=("Courier", 14))
    l.grid(row=8, sticky=W)

    result2 = compute_all_errors(randomList, 1)
    create_labels(result2, 9)

    root.mainloop()
