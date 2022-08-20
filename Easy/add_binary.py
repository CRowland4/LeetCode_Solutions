"""Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself."""

"""First solution is to use Python's built-ins int() and bin() to first convert both numbers to a decimal number, add
them together, then convert the sum back to binary and return that."""


def built_ins(a, b) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]


"""My other solution counts how many times each binary place value is represented (in total) between the two numbers,
and builds a new 'pseudo-binary' number where each digit is how many times that particular place value is represented.
For example, the pseudo-binary number 342 would be 2 * (2 ** 0) + 4 * (2 ** 1) + 3 * (2 ** 2). A decimal number is
then constructed by summing the values in this way, and that decimal is converted to binary via the bin() built-in."""


def pseudo_binary(a: str, b: str) -> str:
    binary_places_count = ''
    while a and b:
        binary_places_count = str(int(a[-1]) + int(b[-1])) + binary_places_count
        a = a[:-1]
        b = b[:-1]

    if a:
        binary_places_count = a + binary_places_count
    elif b:
        binary_places_count = b + binary_places_count

    decimal = 0
    for index, digit in enumerate(binary_places_count[::-1]):
        decimal += int(digit) * (2 ** index)

    return bin(decimal)[2:]


"""There exists a solution where the binary math is done all manually, with 0 help from built-ins, but frankly I have no
interest in diving into those at the present moment."""

