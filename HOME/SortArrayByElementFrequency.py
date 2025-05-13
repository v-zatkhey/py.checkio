from collections.abc import Iterable


def frequency_sort(items: list[str | int]) -> Iterable[str | int]:
    distinct_values = set(items)
    frequency_place = []
    k = len(items)
    for v in distinct_values:
        frequency_place.append({"item": v, "frequency": items.count(v), "first_appearance": items.index(v)})
    frequency_place.sort(key=lambda x: k*x["frequency"] - x["first_appearance"], reverse=True)
    result = []
    for i in frequency_place:
        for n in range(i["frequency"]):
            result.append(i["item"])
    return result


print("Example:")
print(list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])))

# These "asserts" are used for self-checking
assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 2, 2, 2, 6, 6]
assert list(frequency_sort(["bob", "bob", "carl", "alex", "bob"])) == [
    "bob",
    "bob",
    "bob",
    "carl",
    "alex",
]
assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
assert list(frequency_sort([])) == []
assert list(frequency_sort([1])) == [1]

print("The mission is done! Click 'Check Solution' to earn rewards!")
