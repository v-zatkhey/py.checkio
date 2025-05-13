from typing import Any, Iterable


def split_list(items: list[Any]) -> Iterable[list[Any]]:
    items_length = len(items)
    if items_length == 0:
        return [[], []]
    middle_idx = items_length // 2 + items_length % 2
    return [items[:middle_idx], items[middle_idx:]]


print("Example:")
print(list(split_list([1, 2, 3, 4, 5, 6])))
print(list(split_list([1, 2, 3])))

assert list(split_list([1, 2, 3, 4, 5, 6])) == [[1, 2, 3], [4, 5, 6]]
assert list(split_list([1, 2, 3])) == [[1, 2], [3]]
assert list(split_list(["banana", "apple", "orange", "cherry", "watermelon"])) == [
    ["banana", "apple", "orange"],
    ["cherry", "watermelon"],
]
assert list(split_list([1])) == [[1], []]
assert list(split_list([])) == [[], []]

print("The mission is done! Click 'Check Solution' to earn rewards!")
