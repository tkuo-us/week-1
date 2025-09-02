# Utility functions for exercises
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

# Check for balanced parentheses
def parentheses(string):
    count = 0
    for char in string:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0

