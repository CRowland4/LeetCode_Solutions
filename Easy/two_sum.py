"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists."""


from typing import List


"""The idea here is to pick the very first element in the list, and then start scanning all elements ahead of it for an 
element that sums with it to the target number. If no element is found, then pick the second element, and start scanning all the 
elements ahead of it, etc. If at any point in this process two elements are found that sum to the target element, those
two elements' indices are immediately returned by the function, ensuring no wasted calculations.

I believe this is O(nlog(n))."""


def two_sum(nums: List[int], target: int) -> List[int]:
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums[i + 1:], start=i + 1):
            if num1 + num2 == target:
                return [i, j]


# Better solution after looking at other algorithms
"""Here we use memoization for a more efficient algorithm. Each number in the list necessarily has another number
that would serve as a solution. So if I have x in my list, the number y where y = target - x would be a solution, if of 
course y was also in the list.

So we start with the first element in the list (x), and search the memo to see if its counterpart, y = target - x, has 
already been passed over and stored.
- If it has, we return the index of our element x, and of y, whose index
we stored when we came across it in the list.
- If it has not, we store our number x and its index in our memo and continue with the next number in our original list.

I believe this is O(n).
"""


def two_sum_better(nums, target):
    memo = {}  # {<num>: <num index>}

    for i, num in enumerate(nums):
        if target - num in memo:
            return [memo[target - num], i]
        else:
            memo[num] = i

