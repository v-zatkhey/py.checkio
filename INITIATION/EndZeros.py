def end_zeros(a: int) -> int:
    number = str(a)
    cnt = 0
    for i in range(len(number)):
        if number[-1-i] == '0':
            cnt = cnt + 1
        else:
            break
    return cnt


print("Example:")
print(end_zeros(10))

# These "asserts" are used for self-checking
assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
