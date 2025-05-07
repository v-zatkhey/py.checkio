def get_direction(a,b):
    if a == b:
        return 0
    else:
        if b > a:
            return 1
        else:
            return -1

def changing_direction(elements: list[int]) -> int:
    direction_chg = 0
    cur_direction = 0
    for i in range(len(elements) -1):
        new_direction = get_direction(elements[i], elements[i+1])
        if cur_direction == 0:
            cur_direction = new_direction
        else:
            if cur_direction * new_direction < 0:
                direction_chg += 1
                cur_direction = new_direction
    return direction_chg


print("Example:")
print(changing_direction([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
