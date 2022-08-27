"""The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.



Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021


Constraints:

1 <= num.length <= 104
0 <= num[i] <= 9
num does not contain any leading zeros except for the zero itself.
1 <= k <= 104"""
from typing import List

"""My solution is the following steps in order: convert the ints in num to a string and join that string together, then
turn that string into an int and add k to it, then put the digits of the sum back into a list, and use map to turn them
back into ints."""


def addToArrayForm(num: List[int], k: int) -> List[int]:
    num_int = int(''.join(list(map(str, num))))
    solution_string_list = list(str(num_int + k))

    return list(map(int, solution_string_list))


"""I'm not going to be writing any manual schoolbook algorithims, I just don't think it's worth my time."""

# After looking
