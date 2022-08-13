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
Any valid string containing these different types of parenthesis will eventually be reduced down to an empty string by
removing these pairs. With each iteration, we check to see if the string is empty (in which case we return True, because
the string was composed fully of valid combinations of those symbols), or if the 'cleaned' string hasn't changed (in
which case we return False)."""


def is_valid(s: str) -> bool:
    while True:
        trimmed_s = s.replace('()', '').replace('[]', '').replace('{}', '')
        if not trimmed_s:
            return True
        elif trimmed_s == s:
            return False
        else:
            s = trimmed_s


# Faster solution from others' submissions
"""In this solution we loop through the initial string and check to see if the current parenthesis closes the previous
one. If it does not, we add the current parenthesis to the stack. If the current parenthesis does close the previous
one, we remove the previous one from the stack, and don't add the current one. After looping through the entire initial
string, we check to see if there are any remaining, unclosed parenthesis in the stack. If there are, we return False,
and if the stack is empty, we return True.
"""


def is_valid_faster(s):
    close_to_open = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = []
    for char in s:
        if stack and close_to_open.get(char) == stack[-1]:
            stack.pop()
        else:
            stack.append(char)

    return not stack
