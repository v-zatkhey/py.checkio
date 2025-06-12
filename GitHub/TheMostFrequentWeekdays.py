from calendar import isleap, day_name
from datetime import date

def most_frequent_days(a):
    first_day = date(a,1,1).weekday()
    result = [day_name[first_day]]

    if isleap(a):
        if first_day == 6:
            result = [day_name[0]] + result
        else:
            result = result + [day_name[first_day + 1]]

    return result


if __name__ == "__main__":
    print("Example:")
    print(most_frequent_days(1084))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert most_frequent_days(1084) == ["Tuesday", "Wednesday"]
    assert most_frequent_days(1167) == ["Sunday"]
    assert most_frequent_days(1216) == ["Friday", "Saturday"]
    assert most_frequent_days(1492) == ["Friday", "Saturday"]
    assert most_frequent_days(1770) == ["Monday"]
    assert most_frequent_days(1785) == ["Saturday"]
    assert most_frequent_days(212) == ["Wednesday", "Thursday"]
    assert most_frequent_days(1) == ["Monday"]
    assert most_frequent_days(2135) == ["Saturday"]
    assert most_frequent_days(3043) == ["Sunday"]
    assert most_frequent_days(2001) == ["Monday"]
    assert most_frequent_days(3150) == ["Sunday"]
    assert most_frequent_days(3230) == ["Tuesday"]
    assert most_frequent_days(328) == ["Monday", "Sunday"]
    assert most_frequent_days(2016) == ["Friday", "Saturday"]
    print("Coding complete? Click 'Check' to earn cool rewards!")
