def is_even(num: int) -> bool:
    return  True if num % 2 == 0 else False

# def is_even(num: int) -> bool:
#     return num & 1 == 0

print("Example:")
print(is_even(2))

# These "asserts" are used for self-checking
assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
