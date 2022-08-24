"""A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the
minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

For example, the below binary watch reads "4:51".


Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all
possible times the watch could represent. You may return the answer in any order.

The hour must not contain a leading zero.

For example, "01:00" is not valid. It should be "1:00".
The minute must be consist of two digits and may contain a leading zero.

For example, "10:2" is not valid. It should be "10:02".


Example 1:

Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
Example 2:

Input: turnedOn = 9
Output: []


Constraints:

0 <= turnedOn <= 10"""

"""My first solution is to convert each of the possible LEDs into seconds, and hard-code those values into a list. Then
we generate all possible turnedOn-combos with the itertools.combinations() function. We then iterate through all of the
possible combinations (excluding combos that include all of the 32, 16, 8, and 4 minute values, as these just all add up
to an hour), sum up the total seconds in each combo, and use timedelta from datetime to convert the seconds into a
timestamp. We strip the seconds value off of this timestamp and filter out times greater than or equal to 12:00, and
return the list full of the rest."""


class Solution:
    def readBinaryWatch(self, turnedOn):
        from datetime import timedelta
        from itertools import combinations

        if not 0 <= turnedOn <= 8:
            return []

        button_seconds = [28800, 14400, 7200, 3600, 1920, 960, 480, 240, 120, 60]

        possible_times = []
        for combo in combinations(button_seconds, turnedOn):
            if self.is_bad_combo(combo):
                continue
            total_seconds = sum(combo)
            time_stamp = str(timedelta(seconds=total_seconds))[:-3]  # Cut off seconds
            if int(time_stamp[:time_stamp.index(':')]) < 12:
                possible_times.append(time_stamp)

        return possible_times

    def is_bad_combo(self, combo):
        c1 = 1920 in combo
        c2 = 960 in combo
        c3 = 480 in combo
        c4 = 240 in combo

        return c1 and c2 and c3 and c4


# After looking
"""Found a totally brilliant solution that I love. The watch is binary, so the watch's LEDs can be exactly represented
by a 10-digit binary number. So we can loop through all possible times between 00:00 and 11:59, and see which one of
their binary representations has exactly n=turnedOn 1s in it. Then we append those times to a list. This is one of my
favorite solutions to any problem I've seen on LeetCode."""


def readBinaryWatch(turnedOn):
    times = []
    for hour in range(12):
        for minute in range(60):
            if (bin(hour) + bin(minute)).count('1') == turnedOn:
                times.append('%d:%02d' % (hour, minute))
    return times
