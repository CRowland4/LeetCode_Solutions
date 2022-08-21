"""Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?"""

"""My first solution is recursive, and is self-explanatory. Detailing it here would basically be rewriting the code."""


def recursive(root):
    if not root:
        return root

    result = []

    def in_order(new_root):
        if not new_root.left and not new_root.right:
            result.append(new_root.val)
        elif not new_root.left and new_root.right:
            result.append(new_root.val)
            in_order(new_root.right)
        elif new_root.left and not new_root.right:
            in_order(new_root.left)
            result.append(new_root.val)
        elif new_root.left and new_root.right:
            in_order(new_root.left)
            result.append(new_root.val)
            in_order(new_root.right)

        return result

    return in_order(root)


"""My next solution is iterative, rather than recursive, per the followup challenge. The explanation is detailed in the
comments."""


def iterative(root):
    if not root:  # Check for a non-empty tree
        return root

    result = []
    nodes = [root]
    while nodes:
        current = nodes[-1]

        # If the current node has no children, append its value to the result and flag it as used.
        if not current.left and not current.right:
            result.append(current.val)
            current.val += 201  # The constraint said that -100 <= value <= 100, so this will let us know that this node's value has already been read into our result
            nodes.pop()  # We've read this node's value, so remove it from the list

        elif current.left and not current.right:
            if current.left.val > 100:  # If the left node of this current node has already been read into our result
                current.left = None  # Set it to None so this block won't be triggered on the next iteration
            else:
                nodes.append(current.left)  # The left child node will be our next 'current' node.

        elif not current.left and current.right:
            if current.val > 100:  # If we've already read our current node's value into the result
                nodes.pop()  # Remove it from the list of nodes
            elif current.right.val <= 100:  # If we haven't read the right child node's value into the result yet
                result.append(current.val)  # Read the current value into our result
                current.val += 201  # Mark it as read
                nodes.append(current.right)  # The right child node will be our next 'current' node.
            elif current.right.val > 100:  # If the right node of this current node has already been read into result
                current.right = None  # Set it to None so this block won't be triggered on the next iteration.

        elif current.left and current.right:  # If both child nodes exist
            if current.left.val > 100:  # If we've already used the left one's value, set the left node to None to avoid this block in future iterations
                current.left = None
            else:  # The left child node will be our next 'current' node.
                nodes.append(current.left)

    return result


# After looking.
"""There is a far cleaner way to use a recursive solution. I just had extra, unnecessary logic."""


def recursion_v2(root):
    result = []

    def in_order(node):
        if not node:
            return

        in_order(node.left)
        result.append(node.val)
        in_order(node.right)
        return result

    return in_order(root)


"""There was also a much easier way to employ the iterative solution."""


def iterative_v2(root):
    if not root:
        return

    result = []
    stack = []
    while True:

        while root:
            stack.append(root)
            root = root.left

        if not stack:
            return result

        node = stack.pop()
        result.append(node.val)

        if node.right:
            root = node.right

