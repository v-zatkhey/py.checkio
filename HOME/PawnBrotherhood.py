def pawn_capture(pawn: str) -> set:
    may_capture = set()
    if pawn[1] == "8":
        return may_capture
    row_num = str(int(pawn[1])+1)
    if pawn[0] != "a":
        may_capture.add(chr(ord(pawn[0]) - 1) + row_num)
    if pawn[0] != "h":
        may_capture.add(chr(ord(pawn[0]) + 1) + row_num)
    return may_capture

def safe_pawns(pawns: set) -> int:
    safe_squares = set()
    for p in pawns:
        safe_squares = safe_squares.union(pawn_capture(p))
    return sum(map(lambda x: x in safe_squares, pawns))


print("Example:")
print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))

assert safe_pawns({"f4", "g5", "c3", "d2", "b4", "e3", "d4"}) == 6
assert safe_pawns({"f4", "e5", "g4", "e4", "b4", "d4", "c4"}) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
