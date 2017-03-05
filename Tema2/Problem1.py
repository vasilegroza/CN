import numpy as np
from tkinter import *
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



print('solutia este:' ,x)
print(A)

for i in range(n):
    for j in range(i+1, n):
        A[j][i]= A[i][j]
print(A)
print("*************************")
L = np.linalg.cholesky(np.array(A))
print(L)
print('Solutia aplicand algoritmul din libraria numpy este:')
print(np.linalg.solve(A,b))
print("*************************")
distances = np.subtract(np.dot(A,x),b)

print(sum([abs(d) for d in distances]))

def solve(t:Text):
    print("work starts...")
    print(t.get("1.0",END))
    # print(t.get())
    pass

root = Tk()

root.wm_title("Tema2")
root.geometry('{}x{}'.format(400, 400))

t = Text(root, height=5, width=20)
Button(root, text="Apasa", command = lambda : solve(t)).grid()
v = StringVar()
l = Label(root, text="Matrix A")
l.grid(row=1,column=0)
t.grid(padx = 10)
root.mainloop()
