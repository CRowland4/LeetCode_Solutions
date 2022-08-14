"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order."""


# Required class for problem.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""HELPFUL NOTE TO SELF: You need to think about having a reference pointing at the ListNode objects, rather than just
trying to manipulate the objects themselves directly. We'll see if this helps when I come back to this."""

"""My first solution starts with a blank ListNode. It then compares the values of the current nodes of list1
and list2, and takes the lesser of the two (or the first if they are equal) and assigns it to the value of the current
solution node. The solution reference 'next' attribute is then reassigned accordingly, along with the reference to the 
list whose value was selected. Once one of the lists is exhausted, what is left of the remaining list is attached to the
end of the solution reference, and the head of solution is returned."""


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    solution = ListNode()
    solution_reference = solution

    if not (list1 or list2):  # Edge case where both list heads are empty. Could also have returned list2.
        return list1

    while list1 and list2:
        if list1.val <= list2.val:
            solution_reference.val = list1.val
            list1 = list1.next
        elif list2.val <= list2.val:
            solution_reference.val = list2.val
            list2 = list2.next

        solution_reference.next = ListNode()
        solution_reference = solution_reference.next

    if list1:
        solution_reference.val = list1.val
        solution_reference.next = list1.next
    elif list2:
        solution_reference.val = list2.val
        solution_reference.next = list2.next

    return solution


# After looking at other solutions.
"""My solution was pretty close to the optimal solution, it could just be streamlined. That's what's below."""


def streamlined(list1, list2):
    solution = ListNode()
    solution_reference = solution

    while list1 and list2:
        if list1.val < list2.val:
            solution_reference.next = list1
            list1 = list1.next
        else:
            solution_reference.next = list2
            list2 = list2.next

        solution_reference = solution_reference.next

    if list1:
        solution_reference.next = list1
    elif list2:
        solution_reference.next = list2

    return solution.next  # Since we didn't reassign the .val attribute, .next is actually where the solution 'head' is.
