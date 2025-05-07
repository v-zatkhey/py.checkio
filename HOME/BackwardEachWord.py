def reverse(word: str) -> str:
    result = ""
    for i in range(len(word)):
        result = result + word[-(i+1)]
    return result

def backward_string_by_word(text: str) -> str:
    current_word = ""
    result = ""
    for i in range(len(text)):
        if text[i] == " ":
            if current_word == "":
                result = result + text[i]
            else:
                result = result + reverse(current_word) + text[i]
                current_word = ""
        else:
            current_word = current_word + text[i]

    if current_word != "":
        result = result + reverse(current_word)

    return result


print("Example:")
print(backward_string_by_word(""))

# These "asserts" are used for self-checking
assert backward_string_by_word("") == ""
assert backward_string_by_word("world") == "dlrow"
assert backward_string_by_word("hello world") == "olleh dlrow"
assert backward_string_by_word("hello   world") == "olleh   dlrow"
assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"

print("The mission is done! Click 'Check Solution' to earn rewards!")
