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
        pass

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


    def compute_norm(self):
        distances = np.subtract(np.dot(self.a,self.x_cho),self.b)
        print(sum([abs(d) for d in distances]))

    def solve(t: Text):
        print("work starts...")
        print(t.get("1.0", END))
        # print(t.get())
        pass

if __name__=="__main__":
    root = Tk()
    t1 = Text(root, height=5, width=20)
    t2 = Text(root, height=5, width=20)
    matrixsolver =  MatrixSolver(root, t1, t2)
    matrixsolver.read_from_file("input.txt")
    matrixsolver.cholesk()
    matrixsolver.find_x()
    matrixsolver.lu_decomposition()
    matrixsolver.compute_norm()
# root.wm_title("tema2")
# root.geometry('{}x{}'.format(400, 400))
#
# t = text(root, height=5, width=20)
# button(root, text="apasa", command = lambda : solve(t)).grid()
# v = stringvar()
# l = label(root, text="matrix a")
# l.grid(row=1,column=0)
# t.grid(padx = 10)
# create a frame for the text and scrollbar
    txt_frm = Frame(root, width=600, height=600)
    txt_frm.pack(fill="both", expand=True)
    # ensure a consistent gui size
    txt_frm.grid_propagate(False)
    # implement stretchability
    txt_frm.grid_rowconfigure(0, weight=1)
    txt_frm.grid_columnconfigure(0, weight=1)

    # create a text widget
    txt = Text(txt_frm, borderwidth=3, relief="sunken")
    txt.config(font=("consolas", 12), undo=True, wrap='word')
    txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

    # create a scrollbar and associate it with txt
    scrollb = Scrollbar(txt_frm, command=txt.yview)
    scrollb.grid(row=0, column=1, sticky='nsew')
    txt['yscrollcommand'] = scrollb.set
    root.mainloop()
