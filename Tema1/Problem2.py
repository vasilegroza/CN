import random
from Problem1 import compute_u
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

    print("Asociativitatea nu mai este justa pentru x =", x)
    print('{left} != {right} => {result}'.format(left=left_sum,
                                                 right=right_sum,
                                                 result=found))

    print('{left} != {right} => {result}'.format(left=left_pro,
                                                 right=right_pro,
                                                 result=found))
if __name__ == "__main__":
    m,u = compute_u()
    check_associativity(u)
