from collections.abc import Iterable


def frequency_sorting(numbers: list[int]) -> Iterable[int]:
    frequency = {}
    for i in numbers:
        frequency.update({i:numbers.count(i)})
    numbers.sort(key=lambda x: (frequency[x], -x), reverse=True)
    return numbers

print("Example:")
print(list(frequency_sorting([1, 2, 3, 4, 5])))

# These "asserts" are used for self-checking
assert list(frequency_sorting([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
assert list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])) == [
    4,
    4,
    4,
    3,
    3,
    11,
    11,
    7,
    13,
]
assert list(frequency_sorting([5, 6, 13, 99, 45, 34, 99, 6, 6, 45])) == [6, 6, 6, 45, 45, 99, 99, 5, 13, 34]
print("The mission is done! Click 'Check Solution' to earn rewards!")
