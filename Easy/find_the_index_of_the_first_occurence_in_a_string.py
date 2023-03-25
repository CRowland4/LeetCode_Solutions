"""Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters."""


"""My first solution is to use the built-in index function, and use a try/except block to return -1 if a ValueError is
thrown because <needle> is not in <haystack>"""


def strStr(haystack: str, needle: str) -> int:
    try:
        return haystack.index(needle)
    except ValueError:
        return -1


"""Forgot about the .find() string method, that returns -1 automatically if the <needle> is not in <haystack>,
eliminating the need for the try/except block."""


def strStr2(haystack: str, needle: str) -> int:
    return haystack.find(needle)
