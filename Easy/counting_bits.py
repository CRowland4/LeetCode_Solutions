"""Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number
of 1's in the binary representation of i.



Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101


Constraints:

0 <= n <= 105


Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and
possibly in a single pass? Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)? """

"""For each number less than or equal to n, convert it to binary, then count the number of 1s in the binary string and
append that count to our result list."""


def countBits(n: int):
    bit_counts = []
    for i in range(n + 1):
        bit_counts.append(bin(i).count('1'))

    return bit_counts


# After looking
"""Another pretty great solution with bits. The difference between any two consecutive numbers' binary 
representations is a matter of 1, of course, so you can get one number's binary representation's amount of 1s by 
comparing it with the binary representation of the number preceding it with a & operator, and adding one to account 
for the extra bit that was changed from a zero somewhere. Any number n-1 will have all but 1 of the same ones that n has.
I could definitely improve on bitwise operational awareness. """


def countBits(n: int):
    bit_count = [0]
    for i in range(1, n + 1):
        bit_count.append(bit_count[i & i - 1] + 1)
    return bit_count
