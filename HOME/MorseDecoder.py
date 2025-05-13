MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}

def decode_word(word: str) -> str:
    result = ""
    for code in word.split(" "):
        result = result + MORSE[code]
    return result

def morse_decoder(code: str) -> str:
    code_words = code.split("   ")
    phrase = ""
    for i in range(len(code_words)):
        word = decode_word(code_words[i])
        if i == 0:
            first_letter = word[0].upper()
            if len(word) > 1:
                word = first_letter + word[1:]
            else:
                word = first_letter
            phrase = phrase + word
        else:
            phrase = phrase + " " + word

    # your code here
    return phrase


print("Example:")
print(morse_decoder("... --- -- .   - . -..- -"))

# These "asserts" are used for self-checking
assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
assert (
    morse_decoder("..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----")
    == "I was born in 1990"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
