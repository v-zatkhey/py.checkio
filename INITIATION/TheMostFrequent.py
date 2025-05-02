def most_frequent(data: list[str]) -> str:
    items = set(data)
    res = ''
    res_count = 0
    for i in items:
        i_cnt = data.count(i)
        if i_cnt > res_count:
            res = i
            res_count = i_cnt
    return res


print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

# These "asserts" are used for self-checking
assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
