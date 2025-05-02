from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    if len(elements) != 0:
        first_element_type = type(elements[0])
        first_element = elements[0]
        if len(elements) > 1:
            for i in range(len(elements) - 1):
                if type( elements[i + 1]) != first_element_type or elements[i + 1] != first_element:
                    return False
    return True

# def all_the_same(elements: List[Any]) -> bool:
#     return len(set(elements)) <= 1

# def all_the_same(elements: List[Any]) -> bool:
#     return all(elements[i]==elements[i+1] for i in range(len(elements)-1))


print("Example:")
print(all_the_same([1, 1, 1]))

# These "asserts" are used for self-checking
assert all_the_same([1, 1, 1]) == True
assert all_the_same([1, 2, 1]) == False
assert all_the_same([1, "a", 1]) == False
assert all_the_same([1, 1, 1, 2]) == False
assert all_the_same([]) == True
assert all_the_same([1]) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
