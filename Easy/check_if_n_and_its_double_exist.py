"""Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N
= 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]


Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
Example 2:

Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.
Example 3:

Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.


Constraints:

2 <= arr.length <= 500
-10^3 <= arr[i] <= 10^3"""

"""Iterate through nums, and check to see if the double of each number is at a different index. Return True if it is,
False if you get through the whole list without a hit."""


def checkIfExist(arr) -> bool:
    for i, num in enumerate(arr):
        if 2 * num in arr[:i] + arr[i + 1:]:
            return True

    return False


# After looking at the hints
"""Use of a hash table. We store what elements we've already iterated over, and for each new element we check if double
the new element or half of the new element is in the table's keys."""


def checkIfExist2(arr) -> bool:
    table = {}

    for i, num in enumerate(arr):
        if 2 * num in table:
            return True
        if num % 2 == 0 and num // 2 in table:
            return True
        table[num] = i

    return False
