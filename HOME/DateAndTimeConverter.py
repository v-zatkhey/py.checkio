from calendar import month_name

def date_time(time: str) -> str:
    date_part = time.split(" ")[0]
    time_part = time.split(" ")[1]
    date_human = (str(int(date_part.split(".")[0]))
                  + " " + month_name[int(date_part.split(".")[1])]
                  + " " + date_part.split(".")[2] + " year")

    time_human = str(int(time_part.split(":")[0])) + " hour"
    if int(time_part.split(":")[0]) != 1:
        time_human = time_human + "s"
    time_human = time_human + " " + str(int(time_part.split(":")[1])) + " minute"
    if int(time_part.split(":")[1]) != 1:
        time_human = time_human + "s"

    return date_human + " " + time_human


print("Example:")
print(date_time("01.01.2000 00:00"))

assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
assert date_time("09.05.1945 06:07") == "9 May 1945 year 6 hours 7 minutes"
assert date_time('09.07.1995 16:01') == '9 July 1995 year 16 hours 1 minute'

print("The mission is done! Click 'Check Solution' to earn rewards!")
