from typing import Union


def sun_angle(time: str) -> Union[float, str]:
    if time >= "6:00" and time <= "18:00":
        return 90.0
    return "I don't see the sun!"


print("Example:")
print(sun_angle("07:00"))

assert sun_angle("07:00") == 15
assert sun_angle("12:15") == 93.75

print("The mission is done! Click 'Check Solution' to earn rewards!")
