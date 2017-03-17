def nice_time(millis):
    """:returns: Nice displaying of time."""
    return "{m} mins, {s} seconds, {mm} millis".format(
        m=str(millis // 1000 // 60),
        s=str(millis // 1000 % 60),
        mm=str(millis % 1000))

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
    metadata[n + 1] = len(val) - 1

    return n, b, d, val, col, metadata


def testing_result(result_val, result_col, result_d,  expected_val, expected_col, expected_d):
    result_ok = True
    for i in range(len(result_val)):
        if (result_val[i] != expected_val[i] and result_col[i] != expected_col[i]):
            print("wrong for i=", i)
            result_ok = False
    for i in range(len(result_d)):
        if result_d[i] != expected_d[i]:
            result_ok = False
    return result_ok


def add_a_b(a_n, a_d, a_val, a_col , b_n, b_d, b_val, b_col ):
    # sa nu uitam sa adunam si  diagonalele


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

        if ((a_new_line or b_new_line) and (row_a == row_b)):
            m1.append(0)
            m3.append(- row_a)
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
    d = [ a_d[i]+b_d[i] for i in range(a_n)]
    aplusb_n, aplusb_b, aplusb_d, aplusb_val, aplusb_col, metadata_aplusb = read_matrix("a+b.txt")
    is_ok = testing_result(m1, m3, d, aplusb_val, aplusb_col, aplusb_d)
    if (is_ok):
        print("a+b=> rezolvat corect ", is_ok)


def multiply_a_b(a_n, a_b, a_d, a_val, a_col, metadata_a, b_n, b_b, b_d, b_val, b_col, metadata_b ):

    delta = [[0 for _ in range(a_n)] for _ in range(a_n)]
    for i in range(a_n):
        delta[i][i] = a_d[i] * b_d[i]
        start_line, end_line = metadata_b[i + 1], metadata_b[i + 2]
        for j in range(start_line + 1, end_line, 1):
            delta[i][int(b_col[j]) - 1] += a_d[i] * b_val[j]

    for a_line, a_line_start in metadata_a.items():
        a_line_end = metadata_a.get(a_line + 1, len(a_val))

        for index_a in range(a_line_start + 1, a_line_end, 1):
            a_column = int(a_col[index_a])
            delta[int(a_line) - 1][a_column-1] += a_val[index_a] * b_d[a_column-1]
            b_line_start, b_line_end = metadata_b[a_column], metadata_b[a_column + 1]
            for index_b in range(b_line_start + 1, b_line_end, 1):
                delta[int(a_line) - 1][int(b_col[index_b]) - 1] += a_val[index_a] * b_val[index_b]

    # postprocess delta, to format val and col
    delta_d = []
    delta_val = []
    delta_col = []
    for i in range(a_n):
        delta_val.append(0)
        delta_col.append(-(i + 1))
        for j in range(a_n):
            if i == j:
                delta_d.append(delta[i][i])
            else:
                if delta[i][j] != 0:
                    delta_val.append(delta[i][j])
                    delta_col.append(j + 1)

    aorib_n, aorib_b, aorib_d, aorib_val, aorib_col, metadata_aorib = read_matrix("aorib.txt")

    is_ok = testing_result(delta_val, delta_col, delta_d, aorib_val, aorib_col, aorib_d)
    if (is_ok):
        print("a*b=> rezolvat corect ", is_ok)
    else:
        print("a*b=> rezolvat gresit ", is_ok)

import time

start_time = time.time()
a_n, a_b, a_d, a_val, a_col, metadata_a = read_matrix("a.txt")
b_n, b_b, b_d, b_val, b_col, metadata_b = read_matrix("b.txt")
add_a_b(a_n, a_d, a_val, a_col , b_n, b_d, b_val, b_col)
multiply_a_b(a_n, a_b, a_d, a_val, a_col, metadata_a, b_n, b_b, b_d, b_val, b_col, metadata_b )
running_time = time.time() - start_time
print("Running time is:{time}".format(time=nice_time(running_time * 1000)))

