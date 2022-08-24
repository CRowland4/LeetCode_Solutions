"""Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace
and initial word order.



Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"


Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space."""

"""My solution is to put split the sentence up into it's respective words, then use reverse string slicing to reverse
them all, then join them back together with a whitespace separator."""


def reverseWords(s):
    reversed_words = [word[::-1] for word in s.split()]
    return ' '.join(reversed_words)


# After looking
"""There are at least two alternate methods that I saw to this, but both are much more manual and not nearly as easy
or readable. None that I care to redo here."""