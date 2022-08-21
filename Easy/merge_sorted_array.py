"""You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To
accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109


Follow up: Can you come up with an algorithm that runs in O(m + n) time?"""

"""My solution uses two pointers, pointer1 for nums1 and pointer 2 for nums2. First we check a couple base conditions:
if nums2 is empty, we immediately return because nums1 will not be changed. If m == 0, we clear the n 0s out of nums1,
copy nums2 into it, and return. If neither of these conditions is met, we start our loop. This solution is O(m + n), as
suggested in the followup challenge.

Each time we insert an element from nums2 into nums1, we increment pointer2 - and since we know we will have to insert
every number from nums2 into nums1 eventually, our loop runs while pointer2 < n, where n is the number of element in
nums2. 

There are three checks in the loop: If our number in nums2 at pointer2 (we'll call it num2 from now one) is less than
or equal to the number in nums1 at pointer1 (we'll call it num1 from now on), we insert num2 into nums1 at pointer1. We
then increment pointer1 by 1, pointer2 by 1, and we'll also increment m by one. We increment m by one so that we have an
indicator of when we've hit the n 0s at the end of nums1. Then we pop the last element off of nums1, which will be a 0.

Then the second check. If we are still within our loop, we know pointer2 is still less than n, therefore we know that we
haven't yet inserted all of the elements from nums2. And if pointer1 >= m (the second check), we know that we've come up
on the end of nums1, and every element from here on out in nums2 will be appended to the 'end' of nums1. But the end
isn't nums1[-1], because of the additional zeroes. So we insert num2 in nums1 at pointer1, then increment pointer1 and
pointer2 by one, and pop another one of the n 0s off of the end of nums1.

The final check is if num2 is bigger than num1. In this case we wouldn't insert num2 in nums1 at pointer1, because it
would be out of order. But we also know we haven't reached the end of the initial m elements in nums1, since check 2
wasn't true. So in this case we just increment pointer1 by 1 and restart the loop. 

This continues until all n elements of nums2 have been inserted into nums1. And since we pop the last element off of
nums1 every time we have an insertion of num2, we know that exactly all of the n 0s at the end of nums1 will be popped
off.
"""


def merge(nums1, m: int, nums2, n: int):
    """Do not return anything. Modify nums1 in place instead."""
    if not nums2:
        return
    elif m == 0:
        nums1.clear()
        nums1.extend(nums2)
        return

    pointer1 = 0
    pointer2 = 0
    while pointer2 < n:
        if nums2[pointer2] <= nums1[pointer1]:
            nums1.insert(pointer1, nums2[pointer2])
            pointer1 += 1
            pointer2 += 1
            m += 1
            nums1.pop()
        elif pointer1 >= m:
            nums1.insert(pointer1, nums2[pointer2])
            pointer2 += 1
            pointer1 += 1
            nums1.pop()
        elif nums2[pointer2] > nums1[pointer1]:
            pointer1 += 1

    return


# After looking
"""I didn't find a totally different solution that seemed to be better than mind, but I did realize after looking at
some others that I didn't need those first two checks. Both of those are handled by the logic within the while loop."""


def merge1(nums1, m: int, nums2, n: int):
    """Do not return anything. Modify nums1 in place instead."""
    pointer1 = 0
    pointer2 = 0
    while pointer2 < n:
        if nums2[pointer2] <= nums1[pointer1]:
            nums1.insert(pointer1, nums2[pointer2])
            pointer1 += 1
            pointer2 += 1
            m += 1
            nums1.pop()
        elif pointer1 >= m:
            nums1.insert(pointer1, nums2[pointer2])
            pointer2 += 1
            pointer1 += 1
            nums1.pop()
        elif nums2[pointer2] > nums1[pointer1]:
            pointer1 += 1

    return
