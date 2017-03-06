import numpy as np
from tkinter import *

class MatrixSolver():
    def __init__(self, root: Tk, txt_input_a: Text, txt_input_b: Text):
        self.root = root
        self.txt_input_a = txt_input_a
        self.txt_input_b = txt_input_b
        self.a =[]
        self.n = 0
        self.b =[]
        self.d =[]
        self.det = 1
    def read_from_file(self, file_name:str):
        with open(file_name,'r') as f:
            self.a = [[float(x) for x in line.split()] for line in f]
        self.b = [1, 2, 3]
        self.n = len(self.a)
        self.d = [0 for x in range(self.n)]
        return True
    def cholesk(self):
        # descompunerea cholesk
        for p in range(self.n):
            s = sum([self.d[k] * (self.a[p][k] ** 2) for k in range(p)])
            self.d[p] = self.a[p][p] - s

            for i in range(p + 1, self.n):
                s = sum([self.d[k] * self.a[i][k] * self.a[p][k] for k in range(p)])

                self.a[i][p] = (self.a[i][p] - s) / self.d[p]
                # a[p][i] = a[i][p]
            self.det *= self.d[p]
        print("A=", self.a)
        print("det = ", self.det)


    def read_from_gui(self):
        a_txt = self.txt_input_a.get("1.0",END)
        b_txt = self.txt_input_b.get("1.0",END)

        self.a = [[float(x) for x in line.split()] for line in a_txt.split('\n') if line !='']
        self.b = [float(x) for x in b_txt.split()]
        self.n = len(self.a)
        self.d = [0 for x in range(self.n)]
        # print(self.a)
        # print(self.b)
        # print('**********************')
    def find_x(self):
        z = [0 for x in range(self.n)]
        y = [0 for x in range(self.n)]
        x = [0 for x in range(self.n)]

        for i in range(self.n):
            z[i] = self.b[i] - sum([self.a[i][j] * z[j] for j in range(i)])

        for i in range(self.n):
            y[i] = z[i] / self.d[i]

        for j in range(self.n - 1, -1, -1):
            x[j] = y[j] - sum([self.a[i][j] * x[i] for i in range(j, self.n)])


        self.x_cho = x
        print("X = ", x)
        return x

    def lu_decomposition(self):
        print("*************************")
        for i in range(self.n):
            for j in range(i + 1, self.n):
                self.a[j][i] = self.a[i][j]
        L = np.linalg.cholesky(np.array(self.a))
        print(L)
        print('solutia aplicand algoritmul din libraria numpy este:')
        print(self.a)
        print(np.linalg.solve(self.a, self.b))
        self.x_numpy = (np.linalg.solve(self.a, self.b))


    def compute_norm(self):
        print("X is")
        print(self.x_cho)
        distances = np.subtract(np.dot(self.a,self.x_cho),self.b)
        print(sum([abs(d) for d in distances]))
        self.norm = sum([abs(d) for d in distances])

    def init_gui(self):
        root.wm_title("tema2")
        root.geometry('{}x{}'.format(600, 400))

        # t = Text(root, height=5, width=20)
        Button(root, text="Apasa", command = lambda : self.solve(self.txt_input_a,
                                                                 self.txt_input_b)).grid()
        l = Label(root, text="matrix A")
        l.grid(row=1,column=0)
        self.txt_input_a.grid(padx = 10)
        l = Label(root, text="Vector B")
        l.grid(row=3, column=0)
        self.txt_input_b.grid(padx=10)

    def solve(self, t1: Text, t2: Text):
        print("work starts...")
        self.read_from_gui()
        # self.read_from_file("input.txt")
        self.cholesk()
        self.find_x()
        self.show_results1()
        self.lu_decomposition()
        self.compute_norm()
        self.show_results2()


        pass
    def show_results1(self):
        Label(root, text="matrix D:").grid(row=1, column=2, padx = 10)
        ld = Label(root, text = str(self.d))
        ld.grid(row = 1, column = 3, padx = 10)

        L = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if i==j:
                    L[i][j]=1
                elif i>j:
                    L[i][j] = self.a[i][j]
                else:
                    L[i][j] = 0
        Label(root, text="matrix L").grid(row = 2, column = 2, padx=10)
        Label(root, text = str(L)).grid(row = 2, column = 3, padx=10)
        Label(root, text="detA =").grid(row=3, column=2, padx=10)
        Label(root, text=str(self.det)).grid(row=3, column=3, padx=10)
        Label(root, text="Solutia determinata este: ").grid(row=4, column=2, padx=10)
        Label(root, text=str(self.x_cho)).grid(row=4, column=3, padx=10)
        pass
    def show_results2(self):
        Label(root, text="Solutia calculata cu numPy: ").grid(row=5, column=2, padx=10)
        Label(root, text=str(self.x_numpy)).grid(row=5, column=3, padx=10)
        Label(root, text="Norma calculata este:: ").grid(row=6, column=2, padx=10)
        Label(root, text=str(self.norm)).grid(row=6, column=3, padx=10)


if __name__=="__main__":
    root = Tk()
    t1 = Text(root, height=5, width=20)
    t2 = Text(root, height=3, width=20)
    matrixsolver =  MatrixSolver(root, t1, t2)
    matrixsolver.init_gui()
    root.mainloop()
