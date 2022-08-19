"""Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr()
and Java's indexOf().

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters."""
import performance_test

"""First solution is to use Python's built-in string method .index() to return the index of needle in haystack. If
needle is not in haystack, .index() will return a ValueError, which we catch and return -1 instead."""


def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    try:
        return haystack.index(needle)
    except ValueError:
        return -1


"""My next solution attempts to construct needle from substrings of haystack. We iterate through the letters of
haystack, checking for the letter that needle starts with. When we find it, we start a new iteration from that point,
adding consecutive letters from haystack to the letter that needle starts with. We check that we are still on the right 
track with every iteration using the string.startswith() method. If we end up constructing needle, we return the index
of our outermost loop, where the substring began. If we add a letter that does not match needle, we break out of the
inner loop and start looking for the first letter of needle again. Potential inefficiencies here include the case where
haystack is just a bunch of repeats of needle[:-1]."""


def str_str(haystack, needle):
    if not needle:
        return 0

    for right, character in enumerate(haystack):
        if needle.startswith(character):

            if character == needle:
                return right

            construction = character
            for letter in haystack[right + 1:]:
                construction += letter
                if construction == needle:
                    return right
                elif needle.startswith(construction):
                    continue
                else:
                    break

    return -1


# After looking
"""Many of the other submission manually check the next n elements of haystack (where len(needle) = n) to see if they
match needle. It's a simple solution, but has a lot of the faster run times on LeetCode (though I know that the LC
timing method is wildly inconsistent, this is still interesting and I'll test it out myself.

Using my performance_test, using the built-in .index() string method is reliably 200+% faster than this method,
unsurprisingly. Built-ins are highly optimized (so I've read)."""


def str_str2(haystack, needle):
    if not needle:
        return 0

    for i in range(len(haystack) + 1 - len(needle)):
        if haystack[i:i + len(needle)] == needle:
            return i

    return -1


performance_test.performance_test(strStr, str_str2, "hello", "ll")