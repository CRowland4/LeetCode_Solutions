"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the
elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space
for space complexity analysis.) """


"""First solution does exactly what you'd expect to do if you were allowed to use division, but I define my own division
function that doesn't use the division operator. Then I realized that this wasn't O(n) because of my division
function."""


def productExceptSelf(nums: list) -> list:
    zero_flag = False
    zeros = nums.count(0)
    if zeros >= 2:
        return [0] * len(nums)
    elif zeros == 1:
        zero_flag = True

    product = 1
    for num in nums:
        if num != 0:
            product *= num

    def div(dividend, divisor):
        left = 1
        right = dividend

        while True:
            mid = int((right + left) * 0.5)
            product = divisor * mid

            if product == dividend:
                return mid
            elif product > dividend:
                right = mid - 1
            else:
                left = mid + 1

    solution = []
    for num in nums:
        if num == 0:
            solution.append(product)
            continue

        if zero_flag:
            solution.append(0)
            continue

        value = div(abs(product), abs(num))
        if num < 0:
            signed_value = value if product < 0 else -value
            solution.append(signed_value)
        elif num > 0:
            signed_value = -value if (product < 0) else value
            solution.append(signed_value)

    return solution


# After looking
"""This solution is 0(n). Make a prefix array such that prefix_array[i] is the product of the numbers up to and
including nums[i]. Then make a postfix array such that postfix_array[i] is the product of the numbers from nums[i]
(inclusive) to the end. Then for the solution array, solution[i] is prefix[i - 1] * postfix[i + 1], so that the ith
number is excluded entirely from the calculation."""


def productExceptSelf_2(nums):
    prefix = []  # Product up to and including number, starting from beginning
    for i, num in enumerate(nums):
        if i == 0:
            prefix.append(num)
        else:
            prefix.append(num * prefix[i - 1])

    postfix = []  # Product up to and including number, starting from end
    for j, num in enumerate(nums[::-1]):
        if j == 0:
            postfix.insert(0, num)
        else:
            postfix.insert(0, num * postfix[0])

    solution = []
    for k in range(len(nums)):
        if k == 0:
            solution.append(postfix[k + 1])
        elif k == len(nums) - 1:
            solution.append(prefix[k - 1])
        else:
            solution.append(prefix[k - 1] * postfix[k + 1])

    return solution


"""Same solution as above, but with O(1) space complexity. This is accomplished by storing the prefix values inside of
the solution array, then replacing them with the product of that same value with the value of the postfix array on the
second pass."""






