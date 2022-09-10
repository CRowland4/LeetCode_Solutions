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

"""My first solution is to loop through the characters in haystack, and see if the next n characters are needle, where n
is the length of needle."""


def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    for i in range(len(haystack) + 1 - len(needle)):
        if haystack[i:i + len(needle)] == needle:
            return i

    return -1


"""Using the .find() method because I forgot it existed earlier."""


def str_Str2(haystack: str, needle: str) -> int:
    return haystack.find(needle)


# After looking
"""Realized I could clean up my first solution by not worrying about indices too much, since string slicing won't return
and IndexError."""


def str_str_3(haystack, needle):
    for i, char in enumerate(haystack):
        if char == needle[0] and haystack[i:i + len(needle)] == needle:
            return i
    return -1
