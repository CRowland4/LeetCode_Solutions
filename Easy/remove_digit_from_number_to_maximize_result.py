"""You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing exactly one occurrence of digit from number such that the value of the
resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in
number.



Example 1:

Input: number = "123", digit = "3"
Output: "12"
Explanation: There is only one '3' in "123". After removing '3', the result is "12".
Example 2:

Input: number = "1231", digit = "1"
Output: "231"
Explanation: We can remove the first '1' to get "231" or remove the second '1' to get "123".
Since 231 > 123, we return "231".
Example 3:

Input: number = "551", digit = "5"
Output: "51"
Explanation: We can remove either the first or second '5' from "551".
Both result in the string "51".


Constraints:

2 <= number.length <= 100
number consists of digits from '1' to '9'.
digit is a digit from '1' to '9'.
digit occurs at least once in number."""


"""Solution is to use the re module to find all occurences of digit in number. Then for each index where digit occurs,
remove digit at that index. Compare the resulting number to your previous maximum and return the biggest."""


def removeDigit(number, digit):
    import re
    indices_of_digit = [match.start() for match in re.finditer(digit, number)]

    max_num = 0
    for i in indices_of_digit:
        new_num = int(number[:i] + number[i + 1:])
        if new_num > max_num:
            max_num = new_num

    return str(max_num)


"""One liner of the same thing because one-liners can be fun."""


def remove_digit_one_liner(number, digit):
    import re
    return str(max([int((number[:i] + number[i + 1:])) for i in [match.start() for match in re.finditer(digit, number)]]))


# After looking
"""The time complexity of this one is the same but it is a different and kinda interesting method. Instead of just
looping through all of number and comparing the results of everything after stripping digit out of all it's occurrences,
this one looks at the value of the next number immediately after digit, and if it's bigger than digit, digit is removed
from that index and the result is immediately returned."""


def remove_digit_value_check(number, digit):
    num_len = len(number)
    last_index = None

    for i, num in enumerate(number):
        if num == digit and i < num_len - 1 and int(number[i + 1]) > int(digit):
            return number[:i] + number[i + 1:]
        elif num == digit:
            last_index = i

    return number[:last_index] + number[last_index + 1:]
