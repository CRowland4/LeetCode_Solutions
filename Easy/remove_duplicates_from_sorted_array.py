"""Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.



Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order."""
from typing import List


"""My first solution loops through the list, and for each item does the following: if there are multiples of that
element, delete one. If not, add one to unique_count and increment the index so we can move on to the next number.
This is very slow, as it calls the count() method for every single element in the list."""


def removeDuplicates(nums: List[int]) -> int:
    unique_count = 0
    i = 0
    while i < len(nums):
        if nums.count(nums[i]) > 1:
            del nums[i]
        else:
            unique_count += 1
            i += 1

    return unique_count


# After looking at other solutions
"""This solution is much more efficient solution and has O(n) time complexity. We start with two pointers, one at the 
first element of the list and one at the second. The general algorithm is this: if the second index is a different 
element than the first, we increment the first pointer by one, and update that index's element to match that of the 
second pointer, then increment the second pointer by one as well. If the elements are the same, our second pointer moves
on to the next element, and the first pointer is untouched we return the index of the first pointer + 1."""


def removeDuplicates2(nums: List[int]) -> int:
    unique_pointer = 0
    for i in range(1, len(nums)):
        if nums[unique_pointer] != nums[i]:
            unique_pointer += 1
            nums[unique_pointer] = nums[i]

    return unique_pointer + 1


"""This is me coming back later and recreating the best solution from my own description of it, then editing my
description based on the problems I had."""


def removeDuplicates3(nums: List[int]) -> int:
    left = 0
    right = 1
    while right < len(nums):
        if nums[right] == nums[left]:
            right += 1
        else:
            left += 1
            nums[left] = nums[right]
            right += 1

    return left + 1
