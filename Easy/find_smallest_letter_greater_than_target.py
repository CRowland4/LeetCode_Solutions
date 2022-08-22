"""Given a characters array letters that is sorted in non-decreasing order and a character target, return the
smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.


Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Example 3:

Input: letters = ["c","f","j"], target = "d"
Output: "f"


Constraints:

2 <= letters.length <= 104
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter."""

"""My solution runs a check based on the fact that the letters wrap, then compares letters in 'letters' until one of
them is larger than the target. This takes advantage of the fact that 'letters' is already sorted in non-decreasing
order. I honestly don't really know how the initial check works in the context of the instructions to this problem,
but oh well. My assumption was that after it 'wraps' around, you start at 27, and that seems to have done the trick."""


def nextGreatestLetter(letters, target):
    if target >= letters[-1]:
        return letters[0]

    for letter in letters:
        if letter > target:
            return letter


"""The next solution is the binary search solution - this is the same solution as the Search Insert Position problem,
except we're using the value ord(letter) rather than the value of the element itself to perform our search. This one
does have a small change though, in that list elements may not be unique. So if our mid pointer happens to land on a letter
whose ord() matches that of target, we find the last occurrence of that letter in the list, and return the letter just
ahead of it."""


def nextGreatestLetter2(letters, target):
    if target >= letters[-1]:
        return letters[0]

    left = 0
    right = len(letters) - 1
    while left <= right:
        mid = (right + left) // 2

        if ord(target) < ord(letters[mid]):
            right = mid - 1
        elif ord(target) > ord(letters[mid]):
            left = mid + 1
        elif ord(target) == ord(letters[mid]):
            return letters[len(letters) - letters[::-1].index(letters[mid])]

    return letters[left]


# After looking
"""My binary solution could be cleaner. Found a great reference on binary variations:
https://www.geeksforgeeks.org/variants-of-binary-search/"""

