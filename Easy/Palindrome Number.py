"""Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-2^31 <= x <= 2^31 - 1"""


"""Here we just convert the given integer to a string, reverse the string, and compare it to the original. If they are
the same, the number is palindromic."""


def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


"""Another solution based on the followup challenge to do the problem without converting the integer to a string.
Here we use integer division to get numbers from each place value and assign them to class attributes.

Based on the constraints, the given number will never be in the 10 billions or higher. So we start by using integer 
division to divide the number by 1 billion, to see how many billions there are. We store the amount of billions, then 
subtract that many billions from our number to drop down to the next lowest place value. The process continues with 100
million, then 10 million, etc., down to the ones.

The list of place values is created and then filtered based on whether or not the values are None (this is what the start_flag attribute is for - 
we don't want to start setting the values as 0 for a place value that is larger than the number itself and end up with something like
'000242' for the number 242, which of course would reverse to '242000' and therefore fail the palindromic test).
The list is then compared to its reverse to determine if the number is palindromic."""


class Solution1:
    x = 0

    ones = None
    tens = None
    hundreds = None
    thousands = None
    ten_thousands = None
    hundred_thousands = None
    millions = None
    ten_millions = None
    hundred_millions = None
    billions = None

    start_flag = False

    @staticmethod
    def is_palindrome(x: int) -> bool:
        Solution1.x = x

        if x < 0:
            return False
        if x < 10:
            return True

        Solution1.set_place_values()

        places = [
            int(place) for place in [Solution1.ones, Solution1.tens, Solution1.hundreds, Solution1.thousands,
                                     Solution1.ten_thousands, Solution1.hundred_thousands, Solution1.millions,
                                     Solution1.ten_millions, Solution1.hundred_millions, Solution1.billions]
            if place is not None
        ]

        reversed_places = list(reversed(places))
        return places == reversed_places

    @classmethod
    def set_place_values(cls):
        cls.helper('billions', 10e8)
        cls.helper('hundred_millions', 10e7)
        cls.helper('ten_millions', 10e6)
        cls.helper('millions', 10e5)
        cls.helper('hundred_thousands', 10e4)
        cls.helper('ten_thousands', 10e3)
        cls.helper('thousands', 10e2)
        cls.helper('hundreds', 10e1)
        cls.helper('tens', 10)
        cls.ones = cls.x if cls.x >= 0 else 0
        return

    @classmethod
    def helper(cls, place, num):
        if cls.x >= num:
            cls.start_flag = True
            setattr(cls, place, cls.x // num)
            place_number = getattr(cls, place)
            cls.x = cls.x - (place_number * num)
        elif cls.start_flag:
            setattr(cls, place, 0)


# Much shorter solution I found after looking at other solutions, that doesn't convert to a string
"""In this solution the number is being reconstructed in reverse order. We start with one variable at """
def is_palindrome1(x):
    if x < 0:
        return False
    else:
        reverse = 0
        while x > 0:
            reverse = reverse * 10 + x % 10
            x = x // 10

    return reverse == x
