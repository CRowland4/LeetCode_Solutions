"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

"""My solution is to continually scrape and remove valid pairs of parentheses/brackets/braces - '()', '[]', and '{}'.
Any valid string of these different types of parenthesis will eventually be reduced down to an empty string by removing
these pairs. With each iteration, we check to see if the string is empty (in which case we return True, because the
string was composed fully of valid combinations of those symbols), or if the 'cleaned' string hasn't changed (in which
case we return False)."""


def is_valid(s: str) -> bool:
    while True:
        trimmed_s = s.replace('()', '').replace('[]', '').replace('{}', '')
        if not trimmed_s:
            return True
        elif trimmed_s == s:
            return False
        else:
            s = trimmed_s

