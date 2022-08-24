"""You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.


Example 1:

Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".
Example 2:

Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.
Example 3:

Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.


Constraints:

3 <= num.length <= 1000
num only consists of digits."""

"""My first solution is to loop through each digit of num, and see if the next two are the same, and compare it to the
previous 3 digit string. The minor complication here comes from the fact that we have to return '000' if that's the only
3 digit string of the same digit in num, so we can't just convert our string to an integer for comparison. There's a few
extra checks to handle that, then we return what we found or, if we found no good strings, an empty string."""


def largestGoodInteger(num):
    max_good_num = ''
    potential = ''

    for i in range(len(num[:-2])):
        if num[i] == num[i + 1] == num[i + 2]:
            potential = num[i] + num[i + 1] + num[i + 2]
        else:
            continue

        if int(potential) == 0 and not max_good_num:
            max_good_num = potential
        elif not max_good_num or int(potential) > int(max_good_num):
            max_good_num = potential

    return max_good_num


"""My next solution is to first collect all of the 3-same-digit substrings, then return the max of them based on their
value when converted to an integer. If the list is empty, return an empty string."""


def largestGoodInteger2(num):
    max_good_nums = []

    for i in range(len(num[:-2])):
        if num[i] == num[i + 1] == num[i + 2]:
            max_good_nums.append(num[i] + num[i + 1] + num[i + 2])

    return max(max_good_nums, key=int) if max_good_nums else ''


# After looking
"""Biggest thing I took from looking at other solutions is that I can just use string comparisons here instead of
turning stuff into an integer. An empty string is always smaller than any other string. This seems to be a bit faster as
well."""


def largestGoodInteger3(num):
    max_good_num = ''

    for i in range(len(num[:-2])):
        if num[i] == num[i + 1] == num[i + 2]:
            number = num[i] + num[i + 1] + num[i + 2]
            max_good_num = number if number > max_good_num else max_good_num

    return max_good_num
