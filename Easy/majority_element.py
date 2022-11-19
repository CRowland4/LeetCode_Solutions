"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109


Follow-up: Could you solve the problem in linear time and in O(1) space?"""


"""Use a defaultdict to store/count the values, then sort the keys of that defaultdict based on their corresponding
values, reverse the sorted list, and return the first element."""


def majorityElement(nums) -> int:
    from collections import defaultdict

    default = defaultdict(int)
    for num in nums:
        default[num] += 1

    sorted_ = sorted(list(default.keys()), key=lambda x: default[x], reverse=True)
    return sorted_[0]
