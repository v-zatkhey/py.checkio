# Taken from mission Acceptable Password I

def is_acceptable_password(password: str) -> bool:
   return len(password)>6 and any(map(lambda i: i.isdigit(), list(password)))


print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
