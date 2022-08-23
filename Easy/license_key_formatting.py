"""You are given a license key represented as a string s that consists of only alphanumeric characters and dashes.
The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group,
which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash
inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

Example 1:

Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:

Input: s = "2-5g-3-J", k = 2 Output: "2-5G-3J" Explanation: The string s has been split into three parts,
each part has 2 characters except the first part as it could be shorter as mentioned above.


Constraints:

1 <= s.length <= 105
s consists of English letters, digits, and dashes '-'.
1 <= k <= 104"""

"""Explained by comments"""


def reformat(s, k):
    s = s.replace('-', '')  # For ease of rearranging
    s = s.upper()

    first_group_length = len(s) % k
    if first_group_length:  # If first_group_length > 0
        new_key = s[:first_group_length] + '-'  # Add the appropriate number of characters to new_key, plus the hyphen
    else:  # If k divides into len(s) evenly, just initialize new_key as an empty string.
        new_key = ''

    s = s[first_group_length:]  # Chop the first group off of s, since it's already been attached to our key
    sections = len(s) // k  # The amount of individual hyphenated sections we'll have, after the first group.

    for _ in range(1, sections + 1):
        new_key += s[:k] + '-'  # Add another set of k characters to our solution, plus a hyphen
        s = s[k:]  # Chop the next k characters from the start of s, since they've already been added to our solution

    return new_key[:-1]  # The last element is a hyphen that we don't want to include.
