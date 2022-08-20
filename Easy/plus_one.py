"""You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the
integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer
does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].


Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's."""
import performance_test

"""Fun solution where I was able to write a one-liner. We turn all of the integers in digits into strings using 
list(map()), join the elements together using .join() with an empty string as the joiner, turn the resultant numeric
string into an integer with int() and add 1, then turn each digit of the numeric string into an integer with map(), and
turn it into a list with list()"""


def one_liner(digits):
    return list(map(int, str(int(''.join(list(map(str, digits)))) + 1)))


"""My next solution is the more algorithmic one, that implements a recursive solution. The base case is that digits is
[9], in which case [1, 0] is returned. If the base case isn't satisfied, we add one to the last integer in the list and
return the list, as long as the last integer isn't 9. If the last digit is 9, we cut it from digits, pass the truncated
digits into our function, add 0 to the end of the result, and that is the solution we return."""


def recursion(digits):
    if digits == [9]:
        return [1, 0]

    if digits[-1] != 9:
        digits[-1] += 1
        return digits
    else:
        return recursion(digits[:-1]) + [0]


"""This solution implements the same general process as the solution above, but this time with memoization instead of
recursion."""


def memoization(digits):
    memo = {
        'digits': digits,
        'zeros': 0
    }

    while True:
        if not memo['digits']:
            return [1] + [0] * memo['zeros']
        elif memo['digits'][-1] != 9:
            memo['digits'][-1] += 1
            return memo['digits'] + [0] * memo['zeros']
        elif memo['digits'][-1] == 9:
            memo['digits'].pop()
            memo['zeros'] += 1

# Recursion is faster than my one-liner for small inputs, but the one liner beats recursion for larger inputs
performance_test.performance_test(recursion, one_liner, [9] * 10)
performance_test.performance_test(recursion, one_liner, [9] * 100)

# And, unsurprisingly, memoization is reliably faster than recursion
performance_test.performance_test(recursion, memoization, [9] * 566)

