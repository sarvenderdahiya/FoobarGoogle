def solution(n):
    num_int = int(n)
    operations = 0
    while num_int > 1:
        if num_int % 2 == 0:
            num_int /= 2
        elif num_int == 3 or ( num_int // 2) % 2 == 0:
            num_int -= 1
        else:
            num_int += 1
        operations += 1

    return operations

print (solution('4'))