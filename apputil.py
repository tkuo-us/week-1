
def palindrome(string):
    cleaned_string = (
        string.lower()
        .replace(",", "")
        .replace(".", "")
        .replace(" ", "")
        .replace(";", "")
        .replace(":", "")
    )
    return cleaned_string == cleaned_string[::-1]

