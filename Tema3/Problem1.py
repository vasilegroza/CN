def remove_empty(element):
    return element != ''


def read_matrix(name):
    fp = open(name)
    lines = list(filter(remove_empty, fp.read().splitlines()))

    n = int(lines[0])
    b = []
    matrix = []
    for ln in lines[1:(n + 1)]:
        b.append(float(ln))

    for ln in lines[(n + 1):]:
        matrix.append([float(i) for i in ln.strip().split(',')])

    matrix.sort(key=lambda x: (x[1], x[2]))

    mat = []
    i = 0
    while i+1 < len(matrix):
        res = matrix[i][0]
        duplicates = False
        while matrix[i][1] == matrix[i+1][1] and matrix[i][2] == matrix[i+1][2]:
            res += matrix[i+1][0]
            duplicates = True
            i += 1
        mat.append((res, matrix[i][1], matrix[i][2]))
        i += 1

    mat.append(matrix[-1])
    matrix = mat

    d = [i[0] for i in filter(lambda x: x[1] == x[2], matrix)]
    matrix = [i for i in filter(lambda x: x[1] != x[2], matrix)]

    val = []
    col = []

    for i in range(0, len(matrix)):
        if i == 0:
            val.append(0)
            col.append(-1)
        elif matrix[i][1] != matrix[i - 1][1]:
            for j in range(int(matrix[i][1] - matrix[i - 1][1]), 0, -1):
                val.append(0)
                col.append((matrix[i][1] + 2 - j) * (-1))
        val.append(matrix[i][0])
        col.append(matrix[i][2]+1)

    val.append(0)
    col.append((n + 1) * -1)

    return n, b, d, val, col


def add_a_b():
    a_n, a_b, a_d, a_val, a_col = read_matrix("a.txt")
    b_n, b_b, b_d, b_val, b_col = read_matrix("b.txt")

    i = 0
    row_a = 0
    j = 0
    row_b = 0
    m1 = []
    m2 = []
    m3 = []
    # cand se termina unul sa termin de adunat si din cealalta matrice

    while i < len(a_val) and j < len(b_val):
        if i + 1 == len(a_val):
            break
        if j + 1 == len(b_val):
            break
        while a_val[i] == 0:
            i += 1
        row_a = a_col[i - 1] * -1

        while b_val[j] == 0:
            j += 1
        row_b = b_col[j - 1] * -1

        if row_a == row_b:
            if a_col[i] == b_col[j]:
                # aux = (a_val[i] + b_val[j], row_a, a_col)
                # matrix.append(aux)
                m1.append(a_val[i] + b_val[j])
                m3.append(a_col)
                i += 1
                j += 1
            elif a_col[i] < b_col[j]:
                # aux = (a_val[i], row_a, a_col)
                # matrix.append(aux)
                m1.append(a_val[i])
                m3.append(a_col[i])
                i += 1
            else:
                # aux = (b_val[j], row_b, b_col)
                # matrix.append(aux)
                m1.append(b_val[j])
                m3.append(b_col[j])
                j += 1
        elif row_a < row_b:
            # aux = (a_val[i], row_a, a_col)
            # matrix.append((a_val[i], row_a, a_col))
            m1.append(a_val[i])
            m3.append(a_col[i])
            i += 1
        else:
            # matrix.append((b_val[j], row_b, b_col))
            m1.append(b_val[j])
            m3.append(b_col[j])
            j += 1

    print("a_val: "+str(a_val[:10]))
    print("a_col: "+str(a_col[:10]))
    print()
    print("b_val: "+str(b_val[:10]))
    print("b_col: "+str(b_col[:10]))

    print(m1[:11])
    print(m3[:11])



add_a_b()

r_n, r_b, r_d, r_val, r_col = read_matrix("a+b.txt")


print()
print(r_val[:11])
print()