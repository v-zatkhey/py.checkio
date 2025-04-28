def first_word(text: str) -> str:
    return text.split(' ')[0]


print("Example:")
print(first_word("Hello world"))

# These "asserts" are used for self-checking
assert first_word("Hello world") == "Hello"
assert first_word("a word") == "a"
assert first_word("greeting from CheckiO Planet") == "greeting"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")

from timeit import timeit as t


def first_word_1(text):
    return text.split(" ")[0]


print(t('first_word_1(x)', setup='x = "asdf we"*10', number=10000, globals=globals()))  # ~2.8 ms
print(t('first_word_1(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()))  # ~1.2 ms
print(t('first_word_1(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()))  # ~37619 ms
print(t('first_word_1(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()))  # ~2225 ms


def first_word_2(text):
    index = text.find(" ")
    return text[:index] if index != -1 else text


print(t('first_word_2(x)', setup='x = "asdf we"*10', number=10000, globals=globals()))  # ~1.6 ms
print(t('first_word_2(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()))  # ~1.1 ms
print(t('first_word_2(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()))  # ~1.6 ms
print(t('first_word_2(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()))  # ~75.8 ms

