# import numpy as np
# from decimal import *
import random
def check_associativity(u):
    found = False
    y = z = u
    left_sum = right_sum = left_pro = right_pro = 0
    while not found:
        x = random.uniform(0,1)
        left_sum = (x + y) + z
        right_sum = x + (y + z)

        left_pro = (x * y) * z
        right_pro = x * (y * z)
        found = left_sum != right_sum and left_pro != right_pro

    print("Asociativitatea nu mai este justa pentru x =",x)
    print('{left} != {right} => {result}'.format(left=left_sum,
                                            right=right_sum,
                                            result=found))

    print('{left} != {right} => {result}'.format(left=left_pro,
                                            right=right_pro,
                                            result=found))


m = 1
u = 0.1
found = True
while 1.0 + u != 1.0:
    u = u / 10.0
    m += 1

print('m =',m - 1)

check_associativity(u)
