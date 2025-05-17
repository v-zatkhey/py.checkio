# Taken from mission All Upper I

def is_all_upper(text: str) -> bool:
    without_space_text = text.replace(" ","")
    if without_space_text == "":
        return False
    return (all(list(map(lambda i: i.capitalize() == i, list(without_space_text)))) and
            any(list(map(lambda i: i.isalpha() , list(without_space_text)))))


print("Example:")
print(is_all_upper("ALL UPPER"))

# These "asserts" are used for self-checking
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == False
assert is_all_upper('     ') == False
assert is_all_upper('123') == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
