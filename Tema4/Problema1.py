import copy
def remove_empty(element):
    return element != ''

def read_matrix(name):
    fp = open(name)
    lines = list(filter(remove_empty, fp.read().splitlines()))

    metadata = {}

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
    while i + 1 < len(matrix):
        matrix_cell = matrix[i][0]
        while matrix[i][1] == matrix[i + 1][1] and matrix[i][2] == matrix[i + 1][2]:
            matrix_cell += matrix[i + 1][0]
            i += 1
        mat.append((matrix_cell, matrix[i][1], matrix[i][2]))
        i += 1
    # adaug ultimul element pentru ca in while el nu este adaugat :):):)
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
            metadata[1] = i
        elif matrix[i][1] != matrix[i - 1][1]:
            for j in range(int(matrix[i][1] - matrix[i - 1][1]), 0, -1):
                val.append(0)
                col.append((matrix[i][1] + 2 - j) * (-1))
                metadata[matrix[i][1] + 2 - j] = len(val) - 1

        val.append(matrix[i][0])
        col.append(matrix[i][2] + 1)

    val.append(0)
    col.append((n + 1) * -1)
    # metadata[n + 1] = len(val) - 1

    return n, b, d, val, col, metadata


def testing_result(result_val, result_col, result_d, expected_val, expected_col, expected_d):
    result_ok = True
    for i in range(len(result_val)):
        if abs(result_val[i] - expected_val[i]) > eps and result_col[i] != expected_col[i]:
            result_ok = False
    for i in range(len(result_d)):
        if abs(result_d[i] - expected_d[i]) > eps:
            result_ok = False
    return result_ok


def add_a_b(a_n, a_d, a_val, a_col, b_n, b_d, b_val, b_col):
    i = 0
    row_a = 0
    j = 0
    row_b = 0
    m1 = []
    m2 = []
    m3 = []
    a_new_line = False
    b_new_line = False
    # cand se termina unul sa termin de adunat si din cealalta matrice

    while i < len(a_val) and j < len(b_val):

        if i + 1 == len(a_val):
            break
        if j + 1 == len(b_val):
            break
        a_new_line = False
        b_new_line = False

        while a_val[i] == 0:
            i += 1
            a_new_line = True

        if a_new_line:
            row_a = a_col[i - 1] * -1

        while b_val[j] == 0:
            j += 1
            b_new_line = True

        if b_new_line:
            row_b = b_col[j - 1] * -1

        if (a_new_line or b_new_line) and (row_a == row_b):
            m1.append(0)
            m3.append(- row_a)
        if row_a == row_b:
            if a_col[i] == b_col[j]:
                m1.append(a_val[i] + b_val[j])
                m3.append(a_col)
                i += 1
                j += 1
            elif a_col[i] < b_col[j]:
                m1.append(a_val[i])
                m3.append(a_col[i])
                i += 1
            else:

                m1.append(b_val[j])
                m3.append(b_col[j])
                j += 1
        elif row_a < row_b:
            m1.append(a_val[i])
            m3.append(a_col[i])
            i += 1
        else:
            m1.append(b_val[j])
            m3.append(b_col[j])
            j += 1

    d = [a_d[i] + b_d[i] for i in range(a_n)]
    aplusb_n, aplusb_b, aplusb_d, aplusb_val, aplusb_col, metadata_aplusb = read_matrix("a+b.txt")
    is_ok = testing_result(m1, m3, d, aplusb_val, aplusb_col, aplusb_d)
    if (is_ok):
        print("A + B=> rezolvat corect ", is_ok)


def multiply_matrix_vector(x, a_n, a_b, a_d, a_val, a_col, metadata_a):
    is_okay = True

    res = []
    for a_line, a_line_start in metadata_a.items():
        # print(a_line)
        a_line_end = metadata_a.get(a_line + 1, len(a_val)-1)
        aux = 0
        for index_a in range(a_line_start + 1, a_line_end, 1):
            aux = aux + a_val[int(index_a)] * x[int(a_col[int(index_a)] - 1)]

        res.append(aux)

    for i in range(a_n):
        res[i] += a_d[i] * x[i]

    return res


def m_gauss_seidel(path):
    n, b, d, val, col, metadata = read_matrix(path)
    x_c = [0 for _ in range(n+1)]
    x_p = [0 for _ in range(n+1)]
    k = 0
    while True:
        x_p = copy.copy(x_c)

        # implementare formula 3
        # print(metadata)
        for line, line_start in metadata.items():
            line_end = metadata.get(line + 1, len(val))
            suma = 0
            for index in range(line_start, line_end, 1):
                column = int(col[index])
                if column<line:
                    suma += val[index] * x_c[column]
                else:
                    suma += val[index] * x_p[column]
            x_c[int(line)] = (b[int(line)-1] - suma)/ d[int(line)-1]


        delta_x = sum([abs(x_p[i] - x_c[i]) for i in range(n + 1)])
        k+=1
        if (delta_x<eps or k>10000 or delta_x>10**8):
            break
    print(k)
    a_ori_x = multiply_matrix_vector(x_c[1:], n,b,d,val,col,metadata)
    error = 0
    if delta_x<eps:
        error = sum([abs(a_ori_x[i]-b[i]) for i in range(n)])
        print(error)
    return delta_x<eps, x_c, error

if __name__ == "__main__":
    eps = 1e-15

    convergent, solutie, total_error = m_gauss_seidel('m_rar_2017_3.txt')
    if convergent:
        print("Solutia gasita are eroarea:", total_error)
    else:
        print("Divergenta")


    pass
