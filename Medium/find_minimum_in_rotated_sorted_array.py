"""Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.



Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.


Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""


# Solution
def findMin(nums) -> int:
    # Standard start for a binary search
    left = 0
    right = len(nums) - 1
    result = nums[0]  # This is an arbitrary start
    while left <= right:  # Standard binary search while loop condition

        if nums[left] < nums[right]:  # This would signify that we're already within a fully sorted array
            result = min(result, nums[left])  # So the min is either going to be the left of the sorted array, or our previous result
            break

        mid = (left + right) // 2  # Define a mid
        result = min(result, nums[mid])  # Consider the mid for the minimum, that way the left/right pointers can be updated without skipping a potential solution

        if nums[left] <= nums[mid]:  # Mid is part of the "left sorted portion" of the array, which won't contain the minimum
            left = mid + 1  # So we update the left pointer, which could mean nums[left:] is fully sorted (which would hit our break condition)
        else:  # Mid is part of the "right sorted portion" of the array
            right = mid - 1  # So we move the right pointer, bringing it closer to the minimum

    return result