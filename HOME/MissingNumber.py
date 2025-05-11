def missing_number(items: list[int]) -> int:
    return (max(items) + min(items)) * (len(items) + 1) // 2 - sum(items)


print("Example:")
print(missing_number([1, 4, 2, 5]))

# These "asserts" are used for self-checking
assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
