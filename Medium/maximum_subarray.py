"""Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer
approach, which is more subtle. """

"""First solution is to use Kadane's Algorithm. If your current sum > 0, add it to the next number in the array, 
and store the new sum. If the next number was positive, then you have a new peak. If the next number was negative, 
then you've already recorded the current peak, which was the previous sum. If your current sum < 0, the next number 
becomes your new starting point. Since sum < 0, it's always true that next > next + sum. If next happens to be 
greater than the current sum, then great, you've started over at a higher position. If next happens to be less than 
sum, then you'll start over lower, but you already have the previous maximum recorderd, and it would have been even 
lower had you combined it with sum, since sum < 0. """


def maxSubArray(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    sums = [nums[0]]
    for num in nums[1:]:
        if sums[-1] > 0:
            sums.append(sums[-1] + num)
        else:
            sums.append(num)

    return max(sums)
