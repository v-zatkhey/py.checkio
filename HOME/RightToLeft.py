def left_join(phrases: tuple[str, ...]) -> str:
    result = ""
    for i in phrases:
        if result != "":
            result = result + ","
        result = result + i.replace("right","left")
    return result


print("Example:")
print(left_join(("left", "right", "left", "stop")))

# These "asserts" are used for self-checking
assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
assert left_join(("brightness wright",)) == "bleftness wleft"
assert left_join(("enough", "jokes")) == "enough,jokes"

print("The mission is done! Click 'Check Solution' to earn rewards!")
