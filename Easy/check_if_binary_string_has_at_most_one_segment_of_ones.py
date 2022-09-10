"""Given a binary string s without leading zeros, return true if s contains at most one contiguous segment of ones.
Otherwise, return false.

Example 1:

Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.
Example 2:

Input: s = "110"
Output: true


Constraints:

1 <= s.length <= 100
s[i] is either '0' or '1'.
s[0] is '1'."""

"""First solution is to have two triggers. The first trigger is set if we find a one. The second trigger is set if we
find a 0 after the first 1. If the second trigger is set and we find another 1, immediately return False. If we don't
find another 1, return True."""


def checkOnesSegment(s: str) -> bool:
    first = False
    zero = False

    for digit in s:
        if not first and digit == '1':
            first = True
        elif first and not zero and digit == '0':
            zero = True
        elif zero and digit == '1':
            return False

    return True


# After looking
"""This solution takes direct advantage of the fact that there are no leading 0s, so the number will always start
with a 1."""


def check_ones_segment(s):
    return '01' not in s
