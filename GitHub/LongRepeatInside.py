def get_repeats(line: str, substring: str) -> str:
    repeat_num = 1
    while line.find(substring * repeat_num) > -1:
        repeat_num += 1
    return '' if repeat_num <= 2 else substring * (repeat_num -1)

def repeat_inside(line: str) -> str:
    result = ''
    for i in range(1, len(line) // 2 + 1): #length of substring
        for j in range(len(line) - i + 1):
            substr_boat = line[j:j + i]
            current_repeats = get_repeats(line, substr_boat)
            if len(current_repeats) > len(result):
                result = current_repeats
    return result

print("Example:")
print(repeat_inside("aaaaa"))

# These "asserts" are used for self-checking
assert repeat_inside("aaaaa") == "aaaaa"
assert repeat_inside("aabbff") == "aa"
assert repeat_inside("aababcc") == "abab"
assert repeat_inside("abc") == ""
assert repeat_inside("abcabcabab") == "abcabc"

print("The mission is done! Click 'Check Solution' to earn rewards!")
