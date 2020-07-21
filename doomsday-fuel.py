from fractions import Fraction

def solution(m):
    mixed_flags = 0  # TO tell if the input has ordered states or mixed states
    encountered_zerosum = 0
    for i in range(len(m)):
        row_sum = 0
        for j in range(len(m[0])):
            row_sum += m[i][j]
        if row_sum == 0:
            encountered_zerosum = 1
        else:
            if encountered_zerosum == 1:
                mixed_flags = 1


    if mixed_flags == 1:
        for row_num in range(len(m[0])):
            rowsum = 0
            for col in m[row_num]:
                rowsum += col
            if rowsum == 0:
                temp_holder = (m.pop(row_num))
                m.append(temp_holder)
                for list in m:
                    element = list.pop(row_num)
                    list.append(element)

    num_source = 0
    num_terminal = 0
    denominators = []
    for row in m:
        term=1
        curr_denom = 0
        for element in row:
            if element > 0:
                curr_denom += element
                term = 0
        denominators.append(curr_denom)
        if term == 0:
            num_source += 1
        else:
            num_terminal += 1
    if num_terminal == len(m):
        return [1,1]
    if num_source == len(m):
        return [0,0]


    source_prob_mat = [[0 for x in range(num_source)] for y in range(num_source)]
    for i in range (0, num_source):
        for j in range (0, num_source):
            source_prob_mat[i][j] = float(m[i][j]) / denominators[i]
   # print(source_prob_mat)


    identity_mat = [[0 for x in range(num_source)] for y in range(num_source)]
    for i in range (0, num_source):
        for j in range (0, num_source):
            if i == j:
                identity_mat[i][j] = 1
            else:
                identity_mat[i][j] = 0


    temp_mat = [[0 for x in range(num_source)] for y in range(num_source)]

    # Subtract source_probab_mat from identity_mat
    for i in range (0, num_source):
        for j in range (0, num_source):
            temp_mat[i][j] = identity_mat[i][j] - source_prob_mat[i][j]
    #print(temp_mat)
    #get inverse of temp_mat
    invert_mat = getMatrixInverse(temp_mat)

    src_to_term_mat = [[0 for x in range(num_terminal)] for y in range(num_source)]
    for i in range (0,num_source):
        for j in range (num_source, num_source + num_terminal):
            src_to_term_mat[i][j-num_source] = float(m[i][j]) / denominators[i]

    #print(invert_mat, "\n")
    # print(src_to_term_mat, "\n")

    # multiply invert_mat with src_to_term_mat
    final_mat =  [[0 for x in range(num_terminal)] for y in range(num_source)]
    for i in range(len(invert_mat)):
        for j in range(len(src_to_term_mat[0])):
            for k in range(len(src_to_term_mat)):
                final_mat[i][j] += invert_mat[i][k] * src_to_term_mat[k][j]

    #print(final_mat)

    terminal_probabilities = [Fraction(i).limit_denominator() for i in final_mat[0]]

    # find the least common denominator
    current_lcd = 1
    for element in terminal_probabilities:
        current_lcd = lcm(current_lcd, element.denominator)

    # change numerators w.r.t least common denominator and append them to the solution
    solution_list = []
    for element in terminal_probabilities:
        solution_list.append(int(element.numerator * current_lcd / element.denominator))

    # append the common denominator to the solution
    solution_list.append(current_lcd)
    #print(terminal_probabilities)
    return solution_list
    #print(solution_list)


def gcd(a, b):
    # Everything divides 0
    if (b == 0):
        return a
    return gcd(b, a % b)

def lcm(a,b):
    lcm = int(a * b / gcd(a,b))
    return lcm

def transposeMatrix(matrix):
    return list(map(list, zip(*matrix)))


def getMatrixMinor(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def getMatrixDeternminant(matrix):
    # base case for 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for c in range(len(matrix)):
        determinant += ((-1) ** c) * matrix[0][c] * getMatrixDeternminant(getMatrixMinor(matrix, 0, c))
    return determinant


def getMatrixInverse(matrix):
    determinant = getMatrixDeternminant(matrix)
    # special case for 2x2 matrix:
    if len(matrix) == 2:
        return [[matrix[1][1] / determinant, -1 * matrix[0][1] / determinant],
                [-1 * matrix[1][0] / determinant, matrix[0][0] / determinant]]

    # find matrix of cofactors
    cofactors = []
    for r in range(len(matrix)):
        cofactorRow = []
        for c in range(len(matrix)):
            minor = getMatrixMinor(matrix, r, c)
            cofactorRow.append(((-1) ** (r + c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant
    return cofactors



#print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))