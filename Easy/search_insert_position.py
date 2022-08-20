"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104"""

"""My first solution uses built-ins. We append the target to nums, sort the list with nums.sort(), then return the
index of target with nums.index(target)."""


def searchInsert(nums, target: int) -> int:
    nums.append(target)
    nums.sort()
    return nums.index(target)


# After looking
"""I absolutely hate binary algorithms, so I'm glad I'll finally have this explanation here to save me from the endless
hell of just-one-off indices and infinite loops. lol.
So we start with left and right pointers at the first and last indices of the list, respectively. Then we run the
following loop until/if left and right overlap.
We set the mid index as the integer-division average of left and right. So when we have an odd number of elements, mid
will be exactly the middle element, and when we have an even number of elements, mid will be the left-center element.
If our target number is identical to the number at mid, we return mid, since our target number would go into that
position and push the existing element at mid to the right.
If our target is bigger than the number at mid, we move our left index to one number past mid, since mid has already
been checked itself.
If our target is smaller than the number at mid, we move our right index to one number before mid, again since mid has
already been checked.
There is the case where our list comes down to two elements, and left ends up bigger than right (run with the test case
of nums = [1, 3] and target = 2). Then we either return mid (target is smaller than nums[mid]) or mid + 1 (target is 
greater than nums[mid]."""


def searchInsert2(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    if target > nums[mid]:
        return mid + 1
    elif target < nums[mid]:
        return mid


"""Same solution as above, just with the excess trimmed off the bottom."""


def searchInsert3(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return left

