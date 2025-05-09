def between_markers(text: str, begin: str, end: str) -> str:
    """
    returns substring between two given markers
    """
    begin_idx = text.find(begin)
    end_idx = text.find(end)

    if begin_idx == -1:
        first_smb_id = 0
    else:
        first_smb_id = begin_idx + len(begin)
    if end_idx == -1:
        last_smb_id = len(text)
    else:
        last_smb_id = end_idx
    if last_smb_id < first_smb_id:
        return ""

    return text[first_smb_id:last_smb_id]


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

assert between_markers("What is >apple<", ">", "<") == "apple"
assert (
    between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
    == "My new site"
)
assert between_markers("No[/b] hi", "[b]", "[/b]") == "No"
assert between_markers("No [b]hi", "[b]", "[/b]") == "hi"
assert between_markers("No hi", "[b]", "[/b]") == "No hi"
assert between_markers("No <hi>", ">", "<") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")
