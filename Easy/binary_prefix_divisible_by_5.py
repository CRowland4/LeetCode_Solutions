"""You are given a binary array nums (0-indexed).

We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to
least-significant-bit).

For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
Return an array of booleans answer where answer[i] is true if xi is divisible by 5.



Example 1:

Input: nums = [0,1,1]
Output: [true,false,false]
Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.
Example 2:

Input: nums = [1,1,1]
Output: [false,false,false]


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1."""
from typing import List

"""My solution is to iterate through nums, and add the string version of the digit to our existing binary string. We
then convert that binary string to a decimal integer, and append to the result list whether or not the decimal is
divisible by 5."""


def prefixesDivBy5(nums: List[int]) -> List[bool]:
    result = []
    bin_string = ''

    for digit in nums:
        bin_string += str(digit)
        result.append(int(bin_string, 2) % 5 == 0)

    return result


# After looking
"""Each time a bit is added on to the left side of an existing binary string, the decimal representation of that number
becomes double what it was previously, plus the new bit, since the new bit is either 0 = 0*2^0 = 0 or 1 = 1*2^0 = 1.
This solution takes advantage of that fact, and is much more efficient as a result."""


def prefixesDivBy5_2(nums: List[int]) -> List[bool]:
    result = []
    current_integer = 0

    for num in nums:
        current_integer = (2 * current_integer) + num
        result.append(current_integer % 5 == 0)

    return result
