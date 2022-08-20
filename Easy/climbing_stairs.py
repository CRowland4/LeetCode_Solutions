"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45"""


"""First solution utilizes memoization. The total number of ways to reach each step is equal to the total ways to 
reach the previous step plus the total number of ways to reach the step two steps back. So we start with the base 
case of 1 way to climb one step and 2 ways to climb 2 steps. Then we build up the memo until we hit n.Pure recursion 
would be super inefficient for this problem, even for relatively small numbers. """


def climbStairs(n: int) -> int:
    memo = {
        1: 1,
        2: 2
    }

    if n in memo:
        return memo[n]

    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]


# After looking
"""Forgot about a cleaner way to handle the memoization, and that's to have a function nested within your outer function
that's responsible for updating the memo and returning the correct values accordingly."""


def climb_stairs_v2(n: int) -> int:
    memo = {
        1: 1,
        2: 2
    }

    def memo_helper(x):
        if x in memo:
            return memo[x]
        else:
            memo[x] = memo_helper(x - 1) + memo_helper(x - 2)
            return memo[x]

    return memo_helper(n)
