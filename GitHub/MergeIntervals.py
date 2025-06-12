def merge_intervals(intervals):
    """
    Merge overlapped intervals.
    """
    result = []
    if len(intervals) == 0:
        return result
    current_interval = list(intervals[0])
    for i in range(len(intervals) - 1):
        if intervals[i + 1][0] - current_interval[1] <= 1:
            current_interval[1] = max(current_interval[1], intervals[i + 1][1])
        else:
            result.append(current_interval)
            current_interval = list(intervals[i + 1])
    result.append(current_interval)
    return list(map(tuple, result))


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)]) == [
        (1, 6),
        (8, 10),
        (12, 19),
    ], "First"
    assert merge_intervals([(1, 12), (2, 3), (4, 7)]) == [(1, 12)], "Second"
    assert merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)]) == [
        (1, 15),
        (17, 20),
    ], "Third"
    print("Done! Go ahead and Check IT")
