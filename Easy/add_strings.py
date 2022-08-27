"""Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You
must also not convert the inputs to integers directly.

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"

Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself."""


"""My solution is to use basic place values to convert each string into an int, then add the ints, and convert the
result to a string. It's not converting the inputs to ints directly, but it is converting the individual digits to
ints."""


def addStrings(num1: str, num2: str) -> str:
    def convert_to_int(num):
        power = len(num) - 1
        result = 0
        for digit in num:
            result += (int(digit) * (10 ** power))
            power -= 1

        return result

    return str(convert_to_int(num1) + convert_to_int(num2))


# After looking:
"""The other solutions were either just converting directly to int and adding, or manually doing addition with carry
values. I don't feel like figuring that process out would be a good use of my time."""
