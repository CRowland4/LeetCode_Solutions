"""The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.



Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1


Constraints:

0 <= x, y <= 231 - 1"""

"""My solution is straightforward - convert both integers to their binary strings (excluding the '0b'), pad the shorter
one to match the length of the longer one, and iterate through the characters of each binary string with zip, adding one
to our result when the characters differ."""


def hammingDistance(x: int, y: int) -> int:
    x_bin = bin(x)[2:]
    y_bin = bin(y)[2:]
    length = max(len(x_bin), len(y_bin))

    result = 0
    for xi, yi in zip(x_bin.zfill(length), y_bin.zfill(length)):
        if xi != yi:
            result += 1

    return result

# After looking
"""This problem was begging for a bitwise XOR solution, and here it is. XOR gives a 1 where bits are different (so one
has a 1 and one has a 0) and a 0 where they are the same (so both 0 or both 1). Therefore the Hamming distance between
two numbers is the amount of 1s in the XOR result."""


def hamming_distance(x, y):
    return bin(x ^ y).count('1')