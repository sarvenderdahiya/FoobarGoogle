def solution(x, y):
    x.sort()
    y.sort()

    xlen = len(x)
    ylen = len(y)

    if xlen > ylen:
        sol = list(set(x) - set(y))
    else:
        sol = list(set(y) - set(x))

    for i in sol:
        x = i
    return x


print(solution([13, 5, 6, 2, 5], [5, 2, 5, 13]))