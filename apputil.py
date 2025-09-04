
def palindrome(string):
    """
    Check if a string is a palindrome, ignoring case and certain punctuation.
    """
    to_remove = [",", ".", " ", ";", ":"]
    cleaned_string = string.lower()
    for char in to_remove:
        cleaned_string = cleaned_string.replace(char, "")
    return cleaned_string == cleaned_string[::-1]

def parentheses(string):
    """
    Check if the parentheses in a string are balanced.
    """
    count = 0
    for char in string:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0

