def how_deep(structure: tuple) -> int:
    if len(structure)==0:
        return 1
    elements_deep = []
    for i in structure:
        if type(i) == tuple:
            elements_deep.append(how_deep(i) + 1)
        else:
            elements_deep.append(1)
    return max(elements_deep)


print("Example:")
print(how_deep((1, 2, 3)))

# These "asserts" are used for self-checking
assert how_deep((1, 2, 3)) == 1
assert how_deep((1, 2, (3,))) == 2
assert how_deep((1, 2, (3, (4,)))) == 3
assert how_deep(()) == 1
assert how_deep(((),)) == 2
assert how_deep((((),),)) == 3
assert how_deep((1, (2,), (3,))) == 2
assert how_deep((1, ((),), (3,))) == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")
