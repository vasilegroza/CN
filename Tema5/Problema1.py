import numpy as np
import copy as cp

A = 0
epsilon = 1e-15
kmax = 10000
n = 3
A = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            A[i][j] = 1
        elif i == j - 1:
            A[i][j] = 2
A = np.matrix(A)
B = A*(-1)


def schultz(v):
    C = np.dot(B, v)
    for i in range(n):
        C[i,i] = C[i, i] + 2

    return np.dot(v,C)


def leeANDlee(V):
    D = np.dot(B, V)
    C = cp.copy(D)
    for i in range(n):
        C[i,i] = C[i, i] + 3

    C = np.dot(D,C)
    for i in range(n):
        C[i, i] = C[i,i] + 3

    return np.dot(V,C)


def leeANDlee2(V):
    D = np.dot(V, B)
    C = cp.copy(D)
    for i in range(n):
        C[i, i] = C[i,i] + 3

    C = np.dot(C, C)

    for i in range(n):
        D[i,i] = D[i, i] + 1

    D = np.dot(D,C)
    D = 1 / 4 * D
    for i in range(n):
        D[i,i] = D[i, i] + 1


    return np.dot(D, V)


def calculeaza_v(fnct):
    pass


if __name__ == "__main__":

    V0 = A.transpose() / (np.linalg.norm(A, 1) * np.linalg.norm(A, np.inf))
    V1 = cp.copy(V0)
    deltaV = 1
    k = 0
    while True:
        if deltaV < epsilon or k > kmax or deltaV > 10 ** 10:
            break

        V0 = cp.copy(V1)

        V1 = leeANDlee2(V0)
        deltaV = np.linalg.norm(V1 - V0)
        k = k + 1

    if deltaV < epsilon:
        print("Am gasit solutia in ", k, " iteratii")
        print (V1)
    else:
        print("Divergenta", k)
