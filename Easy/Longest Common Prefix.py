"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters."""
from typing import List

"""My solution is based on the fact that the longest possible LCP (longest common prefix) of a list of strings is
actually the shortest string in the list. This would happen if every other string in the list started with that
entire particular string. For example, ['go', 'going', 'goth', 'gone', ...], where 'go' is the shortest string, and LCP.

So we start with the first letter of the shortest string, and see if every other string starts with that letter. If they
do, we attach the second letter of the shortest string, and check again. Continue until we've either exhausted all characters from the
shortest string, so therefore the shortest string is the LCP, or we don't get a match, in which case we return the
previous part of the shortest string that had a match on all other strings in our list."""


def longestCommonPrefix(strs: List[str]) -> str:
    prefix = ''
    for character in min(strs, key=len):
        if all([string.startswith(prefix + character) for string in strs]):
            prefix += character
        else:
            break
    return prefix


# After looking at other solutions.
"""I looked at some other solutions and realized that while it's true that the longest potential LCP is the shortest
string in in input list of strings, it's unnecessary to find that string. You can start with any string in the list, and
if the shortest string IS actually the solution, and if you DO start looping through the characters of a longer string,
you'll eventually recreate the shortest string anyway and break out of the loop. So the code below is the same as above,
without the added step of finding the shortest string."""


def longestCommonPrefix_(strs: List[str]) -> str:
    prefix = ''
    for character in strs[0]:
        if all([string.startswith(prefix + character) for string in strs]):
            prefix += character
        else:
            break
    return prefix


"""The code below is another interesting solution I found, that is a bit more efficient. It gets the LCP from the first
two elements in the list, then compares the result with the third element for a new LCP, and so on for every element of
the list. This is due to the basic property that the LCP of thing1, thing2 and thing3 is the same as the LCP of thing1,
and the LCP of thing2 and thing3."""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        lcp = self.lcp_of_two_strings(strs[0], strs[1])
        for string in strs[2:]:
            lcp = self.lcp_of_two_strings(lcp, string)

        return lcp

    def lcp_of_two_strings(self, str1, str2):
        lcp = ''
        for i, character in enumerate(str1):
            try:
                if str2[i] == character:
                    lcp += character
                else:
                    break
            except IndexError:
                break
        return lcp

