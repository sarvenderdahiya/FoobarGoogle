def solution(h,q):
    highest_node_num = (pow (2,h)) - 1
    p = []
    for i in q:
        if (i == highest_node_num):
            p.append(-1)
        else:
            tmp = i
            accumulator = 0
            while ((tmp + 1) & tmp) != 0 and (((tmp + 2) & (tmp + 1)) != 0):
                msb = find_msb(tmp)
                tmp -= (msb - 1)
                accumulator += (msb - 1)

            if (tmp + 1) & tmp == 0:
                tmp = tmp * 2 + 1

            elif (tmp + 2) & (tmp + 1) == 0:
                tmp = tmp + 1

            tmp += accumulator
            p.append(tmp)
    return p

def find_msb(num):
    num |= num >> 1
    num |= num >> 2
    num |= num >> 4
    num |= num >> 8
    num |= num >> 16
    num = num + 1
    num = num >> 1
    return num


print(solution(5, [19,14,28]))


