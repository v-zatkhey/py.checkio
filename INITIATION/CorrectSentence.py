def correct_sentence(text: str) -> str:
    first_smb = text[0]
    last_smb = text[-1]
    if not first_smb.isupper():
        text = first_smb.upper() + text[1:]
    if last_smb != ".":
        text = text + "."
    return text

# def correct_sentence(text: str) -> str:
#     return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")

print("Example:")
print(correct_sentence("greetings, friends"))
print(correct_sentence('welcome to New York'))

# These "asserts" are used for self-checking
assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."
assert correct_sentence('welcome to New York') == 'Welcome to New York.'

print("The mission is done! Click 'Check Solution' to earn rewards!")
