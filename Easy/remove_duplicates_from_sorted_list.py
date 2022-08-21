"""Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the
linked list sorted as well.

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""First solution is to create a dummy pointer at head that we will return once our changes have been made, 
then to walk down the list one by one. We have a pointer 'current_node' and a pointer 'next_node', which is the node 
after 'current_node'. If they both have the same value, we link the current node to the node *after* next_node, 
move the 'next_node' pointer to point to that same node, and repeat until next_node points at None. Base cases are if 
head is None, or if head doesn't have a next node."""


def deleteDuplicates(head):
    if not head or not head.next:
        return head

    dummy = head
    current_node = head
    next_node = dummy.next
    while next_node:
        if current_node.val == next_node.val:
            current_node.next = next_node.next
        else:
            current_node = next_node

        next_node = next_node.next

    return dummy


# After looking
"""This solution is essentially the same, it just uses one pointer instead of two, which makes it a bit shorter. I
honestly don't know if this helps or hurts readability."""


def delete_duplicates(head):
    if not head or not head.next:
        return head

    current_node = head
    while current_node.next:
        if current_node.val == current_node.next.val:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next

    return head
