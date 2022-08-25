"""You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code
of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!



Example 1:

Input: code = [5,7,1,4], k = 3 Output: [12,10,16,13] Explanation: Each number is replaced by the sum of the next 3
numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around. Example 2:

Input: code = [1,2,3,4], k = 0
Output: [0,0,0,0]
Explanation: When k is zero, the numbers are replaced by 0.
Example 3:

Input: code = [2,4,9,3], k = -2 Output: [12,5,6,13] Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice
that the numbers wrap around again. If k is negative, the sum is of the previous numbers.


Constraints:

n == code.length
1 <= n <= 100
1 <= code[i] <= 100
-(n - 1) <= k <= n - 1"""

"""My first solution is to loop through each number and code. For each number, if k is positive, we add each of the next
k numbers together for our entry in the result list. We use the modulus operator to handle the fact that the list wraps.
If k is negative, we just add the previous k elements and we don't need the modulus operator, because accessing a
negative index of a list already loops back from the beginning to the end."""


def decrypt(code, k):
    result = []

    for i, number in enumerate(code):
        new_num = 0

        if k >= 0:
            for j in range(abs(k)):
                new_num += code[(i + j + 1) % len(code)]
        else:
            for m in range(abs(k)):
                new_num += code[(i - m - 1)]

        result.append(new_num)
    return result


"""My next solution is much more efficient, and uses the fact that for each consecutive position in the result, we can
 remove the first number that made up the previous sum, and add the number k units ahead/behind our current position.
 Linear time instead of O(n * k) time."""


def decrypt(code, k):
    result = code.copy()
    n = len(code)

    if k > 0:
        result[0] = sum(code[1:k + 1])

        for i, number in enumerate(result[1:], start=1):
            result[i] = result[i - 1] - number + code[(i + k) % n]

    elif k < 0:
        result[0] = sum(code[-1:k - 1:-1])

        for i, number in enumerate(result[1:], start=1):
            result[i] = result[i - 1] - code[i + k - 1] + code[i - 1]

    elif k == 0:
        return [0] * n

    return result


# After looking
"""Didn't find any other particularly interesting solutions. Some people were adding another copy of code to the end of
code so as to not have to deal with the wrapping, but then still looping one way or another. I think this adds space
complexity, but doesn't actually improve time complexity."""
