from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    length = len(text)
    if length % 2 == 1:
        text = text + "_"
        length += 1

    result = []
    for i in range(length // 2):
        result.append(text[2*i : 2*i + 2])
    return result


print("Example:")
print(list(split_pairs("abcd")))

assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]
assert list(split_pairs("")) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
