"""Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is
returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.



Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.


Constraints:

0 <= x <= 231 - 1"""

"""My first solution is a binary search method (the bane of my existence), with the case of x = 0 or x = 1 accounted for
at the beginning."""


def binary_search(x: int) -> int:
    if x in [0, 1]:
        return x

    left = 0
    right = x
    while left < right:
        mid = (right + left) // 2
        mid_squared = int(mid * mid)

        if x == mid_squared:
            return mid
        elif x < mid_squared:
            right = mid - 1
        elif x > mid_squared:
            left = mid + 1

    return left if left * left <= x else left - 1


# After looking
"""A slightly clearner version, but the same thing overall."""


def binary_search_v2(x: int) -> int:
    if x in [0, 1]:
        return x

    left = 0
    right = x
    while left <= right:
        mid = (right + left) // 2
        mid_squared = int(mid * mid)

        if x == mid_squared:
            return mid
        elif x < mid_squared:
            right = mid - 1
        elif x > mid_squared:
            left = mid + 1

    return right
