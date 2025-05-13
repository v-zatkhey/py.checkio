from typing import Union

def str_to_minutes(time_str: str) -> int:
    return int(time_str.split(":")[0]) * 60 + int(time_str.split(":")[1])

def sun_angle(time: str) -> Union[float, str]:
    time_minutes = str_to_minutes(time)
    sun_rise = str_to_minutes("6:00")
    sun_set = str_to_minutes("18:00")
    if time_minutes >= sun_rise and time_minutes <= sun_set:
        return round(180.0 * ((time_minutes - sun_rise)/(sun_set - sun_rise)), 2)
    return "I don't see the sun!"


print("Example:")
print(sun_angle("07:00"))
print(sun_angle("05:00"))
print(sun_angle("17:59"))


assert sun_angle("07:00") == 15
assert sun_angle("12:15") == 93.75
assert sun_angle("6:00") == 0
assert sun_angle("18:00") == 180
assert sun_angle("15:00") == 135
print("The mission is done! Click 'Check Solution' to earn rewards!")
