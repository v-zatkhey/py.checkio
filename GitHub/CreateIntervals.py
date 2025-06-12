def create_intervals(data):
    result = []
    if len(data)==0:
        return result
    sorted_data = list(data)
    sorted_data.sort()
    current_value = sorted_data[0]
    first_element_of_interval = sorted_data[0]
    for i in range(len(data) -1):
        if sorted_data[i + 1] - current_value == 1:
            current_value = sorted_data[i + 1]
        else:
            result.append((first_element_of_interval, current_value))
            first_element_of_interval = sorted_data[i + 1]
            current_value = sorted_data[i + 1]
    result.append((first_element_of_interval, current_value))

    return result


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [
        (1, 5),
        (7, 8),
        (12, 12),
    ], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print("Almost done! The only thing left to do is to Check it!")
