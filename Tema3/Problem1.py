from numpy.ctypeslib import prep_array


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
        matrix_cell = matrix[i][0]
        while matrix[i][1] == matrix[i+1][1] and matrix[i][2] == matrix[i+1][2]:
            matrix_cell += matrix[i+1][0]
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
        elif matrix[i][1] != matrix[i - 1][1]:
            for j in range(int(matrix[i][1] - matrix[i - 1][1]), 0, -1):
                val.append(0)
                col.append((matrix[i][1] + 2 - j) * (-1))
        val.append(matrix[i][0])
        col.append(matrix[i][2]+1)

    val.append(0)
    col.append((n + 1) * -1)

    return n, b, d, val, col
def testing_result(result_val, result_col, expected_val, expected_col):
    result_ok = True
    for i in range(len(result_val)):
        if(result_val[i]!=expected_val[i] and result_col[i]!=expected_col[i]):
            print("wrong for i=",i)
            result_ok =  False
    return result_ok




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
            row_a = a_col[i - 1]* -1

        while b_val[j] == 0:
            j += 1
            b_new_line = True

        if b_new_line:
            row_b = b_col[j - 1] * -1

        if((a_new_line or b_new_line )and( row_a == row_b )):
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

    aplusb_n, aplusb_b, aplusb_d, aplusb_val, aplusb_col = read_matrix("a+b.txt")
    is_ok = testing_result(m1,m3, aplusb_val, aplusb_col)
    if(is_ok):
        print("a+b=> rezolvat corect ", is_ok)
    # print("a_val: "+str(a_val[:13]))
    # print("a_col: "+str(a_col[:13]))
    # print()
    # print("b_val: "+str(b_val[:13]))
    # print("b_col: "+str(b_col[:13]))
    #
    # print(m1[:100])
    # print(m3[:100])
    #
    # print(str(aplusb_val[:100]))
    # print(str(aplusb_col[:100]))


add_a_b()


#
# # r_n, r_b, r_d, r_val, r_col = read_matrix("a+b.txt")
# r_n, r_b, r_d, r_val, r_col = read_matrix("test.txt")
#
# print(r_n)
# print(r_b)
# print(r_d)
# print(r_val)
# print(r_col)
# # print(r_val[:11])
