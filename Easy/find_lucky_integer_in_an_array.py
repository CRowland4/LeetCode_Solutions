"""Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.



Example 1:

Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
Example 2:

Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
Example 3:

Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.


Constraints:

1 <= arr.length <= 500
1 <= arr[i] <= 500"""

"""Make a collections.Counter object out of the array, and sort the keys of counter by reverse order. Return the first
item from the Counter object whose key is the same as its value, or -1 if none like that are found."""


def findLucky(arr) -> int:
    from collections import Counter

    counter = Counter(arr)
    result = -1
    for num in sorted(counter, reverse=True):
        if counter[num] == num:
            result = num
            return result

    return result


# After looking
"""Other solutions either do basically the same thing with a collections.Counter object, or they build their own
counter."""
