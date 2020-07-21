def solution(start, length):
    pointer = start
    current_xor = 0
    to_skip = -1
    iteration = 0
    while length - iteration > 0:
        next_len = length - iteration
        current_low = pointer
        current_high = current_low + next_len - 1
        pointer = current_high + 1

        new_xor = xor_in_range(current_low, current_high)
        current_xor ^= new_xor

        to_skip += 1
        pointer += to_skip
        iteration += 1
    return current_xor


def xor_in_range(low, high):
    return xor_1_to_n(low - 1) ^ xor_1_to_n(high)


def xor_1_to_n(n):
    mod = n % 4

    if mod == 0:
        return n

    elif mod == 1:
        return 1

    elif mod == 2:
        return n + 1

    elif mod == 3:
        return 0


print(solution(0, 3))

print(solution(17, 4))
