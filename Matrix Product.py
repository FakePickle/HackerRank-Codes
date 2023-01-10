def matrix_mult(m1,m2):
    m3 = [[0 for x in range(len(m2[0]))] for y in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                m3[i][j] += m1[i][k] * m2[k][j]
    return m3