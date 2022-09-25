import performance_test


"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109"""

"""Convert the list to a set (which only allows unique element), then compare that to the length of the original list.
If the lengths are equal, return false, and otherwise true."""


def convert_to_set(nums: list) -> bool:
    return len(set(nums)) != len(nums)


"""Another method using memoization."""


def memoization_with_dict(nums: list) -> bool:
    memo = {}
    for num in nums:
        if num not in memo:
            memo[num] = 0
        else:
            return True

    return False


test_list = [i for i in range(10000)]

for i in range(10):
    performance_test.performance_test(convert_to_set, memoization_with_dict, test_list)


# Unsurprisingly, the built-in method of using len() and set() is faster than using manual memoization.

# After looking
"""Different versions of the same two solutions."""
