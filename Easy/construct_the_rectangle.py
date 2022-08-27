"""A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area,
your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

The area of the rectangular web page you designed must equal to the given target area.
The width W should not be larger than the length L, which means L >= W.
The difference between length L and width W should be as small as possible.
Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.



Example 1:

Input: area = 4 Output: [2,2] Explanation: The target area is 4, and all the possible ways to construct it are [1,4],
[2,2], [4,1]. But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal
compared to [2,2]. So the length L is 2, and the width W is 2. Example 2:

Input: area = 37
Output: [37,1]
Example 3:

Input: area = 122122
Output: [427,286]


Constraints:

1 <= area <= 107"""

"""Start with i at one and j at area. For each iteration of the loop, if i * j == area, add [j, i] to the list of
dimensions (instead of [i, j] because of the condition that L has to be bigger than W). Then we add one to i, and make
j the result of integer division between area and i. Our loop breaks if i > j, to ensure we don't end up checking
the same set of numbers twice."""


def constructRectangle(area: int):
    i = 1
    j = area
    dimensions = []
    while i <= j:
        if i * j == area:
            dimensions.append([j, i])

        i += 1
        j = (area // i)

    return min(dimensions, key=lambda x: x[0])


# After looking
"""Realized that instead of starting the search at the extremes, I could start the search in the 'middle' (at the square
root of area). This way the first result can be returned rather than waiting to find all the possible dimensions then
sorting to find the one that fits the requirements."""


def constructRectangle(area: int):
    import math
    i = int(math.sqrt(area))
    while True:
        if area % i == 0:
            return [area // i, i]

        i -= 1

