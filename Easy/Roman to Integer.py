"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

"""My first solution is to list the possible roman numerals in a dictionary mapping the strings to their integer values,
from largest to smallest. Then we check which one of these values the string starts with (the sorting from largest to 
smallest ensures that we would catch 'CM' and add 900 rather than adding 100 for C and then 1000 for M), add the integer
value of the roman numeral string to our result variable, chop that string off of the start of our initial roman numeral
input, and start over. Repeat this process until the initial roman numeral string is empty, and return the result."""


def romanToInt(s: str) -> int:
    solution = 0

    values = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }

    while s:
        for value in values:
            if s.startswith(value):
                solution += values[value]
                s = s[len(value):]
                break

    return solution


# After looking at other solutions.
"""I'm not sure this one is necessarily better, but it's a different method. The only way a roman numeral with a lower 
value can come before a roman numeral with a higher value is if that lower value should be subtracted from that higher
value. So we loop through each character of the roman numeral, check to see if the following numeral has a higher value,
and add/subtract the current numeral accordingly."""


def roman_to_int(s):
    values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    result = 0
    for i, char in enumerate(s[:-1]):
        if values[char] < values[s[i + 1]]:
            result -= values[char]
        else:
            result += values[char]

    result += values[s[-1]]
    return result