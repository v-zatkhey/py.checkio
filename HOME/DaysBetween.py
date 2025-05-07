from datetime import date

def days_diff(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    a_date = date(a[0], a[1], a[2])
    b_date = date(b[0], b[1], b[2])
    period = abs(b_date - a_date)
    return period.days


print("Example:")
print(days_diff((1982, 4, 19), (1982, 4, 22)))

assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238

print("The mission is done! Click 'Check Solution' to earn rewards!")
