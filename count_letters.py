# Author: Justin Huang
# GitHub username: huangjus
# Date: 2/28/23
# Description: takes a string as input and returns a dictionary that counts the occurrences of
# each uppercase letter in the string. Only uppercase letters are counted,
# and lower-case letters are converted to uppercase before counting.

def count_letters(string):

    """
    Count the occurrences of each uppercase letter in the input string.

    string: The input string.
    """

    counts = {}
    for char in string:
        if char.isupper():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        elif char.islower():
            char_upper = char.upper()
            if char_upper in counts:
                counts[char_upper] += 1
            else:
                counts[char_upper] = 1
    return counts
