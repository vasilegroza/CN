f = open("input.txt")
A = [[float(x) for x in line.split()] for line in f]
b = [1, 2, 3]
n = len(A)
f.close()
d = [0 for x in range(n)]
det = 1

# descompunerea Cholesk
for p in range(n):
    s = sum([d[k] * (A[p][k] ** 2) for k in range(p)])
    d[p] = A[p][p] - s

    for i in range(p+1, n):
        s = sum([d[k] * A[i][k] * A[p][k] for k in range(p)])

        A[i][p] = (A[i][p] - s) / d[p]
        # A[p][i] = A[i][p]
    det *= d[p]


z = [0 for x in range(n)]
y = [0 for x in range(n)]
x = [0 for x in range(n)]

for i in range(n):
    z[i] = b[i] - sum([A[i][j] * z[j] for j in range(i)])

for i in range(n):
    y[i] = z[i] / d[i]

for j in range(n-1, -1, -1):
    x[j] = y[j] - sum([A[i][j] * x[i] for i in range(j, n)])


print(z)
print(x)
print(d)
print(A)