from collections.abc import Iterable


def except_zero(items: list[int]) -> Iterable[int]:
    filtered_items = list(filter(lambda x: x!=0, items))
    filtered_items.sort()
    result = []
    for i in range(len(items)):
        if items[i] == 0:
            result.append(items[i])
        else:
            result.append(filtered_items.pop(0))
    return result


print("Example:")
print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

# These "asserts" are used for self-checking
assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
assert list(except_zero([0, 0])) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")
