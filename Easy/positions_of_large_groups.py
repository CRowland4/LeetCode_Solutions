"""In a string s of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive)
of the group. In the above example, "xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.

Return the intervals of every large group sorted in increasing order by start index.


Example 1:

Input: s = "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the only large group with start index 3 and end index 6.
Example 2:

Input: s = "abc"
Output: []
Explanation: We have groups "a", "b", and "c", none of which are large groups.
Example 3:

Input: s = "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
Explanation: The large groups are "ddd", "eeee", and "bbb".


Constraints:

1 <= s.length <= 1000
s contains lowercase English letters only."""

"""My solution is to use regex group matching. We match any character -- (.) -- and then we match 2 or more MORE of that
same character -- (/1{2,})."""


def largeGroupPositions(s: str):
    import re

    return [[m.start(), m.end() - 1] for m in re.finditer(r"(.)(\1{2,})", s)]


# After looking
"""A two pointer solution. The pointers themselves keep track of the groups, and the condition inside determines how big
a group must be to be added to the solution."""


def largeGroupPositions2(s: str):
    result = []
    i = 0
    for j in range(len(s)):
        if j == len(s) - 1 or s[j] != s[j + 1]:
            if j - i + 1 >= 3:
                result.append([i, j])
            i = j + 1

    return result
