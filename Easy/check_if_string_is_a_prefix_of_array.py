"""Given a string s and an array of strings words, determine whether s is a prefix string of words.

A string s is a prefix string of words if s can be made by concatenating the first k strings in words for some
positive k no larger than words.length.

Return true if s is a prefix string of words, or false otherwise.



Example 1:

Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Output: true
Explanation:
s can be made by concatenating "i", "love", and "leetcode" together.
Example 2:

Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
Output: false
Explanation:
It is impossible to make s using a prefix of arr.


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
1 <= s.length <= 1000
words[i] and s consist of only lowercase English letters."""

"""Initialize an empty string variable. Then for each word in words, concatenate that with your first variable. If the
newly-created string is the same as s, return True. If the newly-created string is longer than s, return False. If you
concatenate the last word in words and neither of those conditions is true, return False."""


def isPrefixString(s: str, words) -> bool:
    comp_string = ''
    for word in words:
        comp_string += word
        if s == comp_string:
            return True
        if len(comp_string) > len(s):
            return False
    return False


# After looking
"""No other totally different methods, but a nice way to optimize."""


def isPrefixString2(s: str, words) -> bool:
    comp_string = ''
    for word in words:
        comp_string += word
        if len(comp_string) == len(s):
            return s == comp_string

    return False

