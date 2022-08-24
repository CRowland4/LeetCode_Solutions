"""Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and
uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.

An English letter b is greater than another letter a if b appears after a in the English alphabet.



Example 1:

Input: s = "lEeTcOdE"
Output: "E"
Explanation:
The letter 'E' is the only letter to appear in both lower and upper case.
Example 2:

Input: s = "arRAzFif"
Output: "R"
Explanation:
The letter 'R' is the greatest letter to appear in both lower and upper case.
Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.
Example 3:

Input: s = "AbCdEfGhIjK"
Output: ""
Explanation:
There is no letter that appears in both lower and upper case.


Constraints:

1 <= s.length <= 1000
s consists of lowercase and uppercase English letters."""

"""My first solution is to make a list of the uppercase versions of all letters whose upper and lowercase versions are
in s. Then we return the 'max' character from that list, where the key is the Unicode index of the letter. An empty
string is returned if there are no letters whose upper and lower case versions appear in s."""


def greatestLetter(s):
    upper_and_lower = [letter.upper() for letter in s if letter.upper() in s and letter.lower() in s]
    return max(upper_and_lower, key=ord) if upper_and_lower else ''


# After looking
"""Found out that I don't need the key=ord part, as the default sorting order does basically the same thing. Other than
that, didn't see any other super interesting solutions."""


def greatestLetter(s):
    upper_and_lower = [letter.upper() for letter in s if letter.upper() in s and letter.lower() in s]
    return max(upper_and_lower) if upper_and_lower else ''
