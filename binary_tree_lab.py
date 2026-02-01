from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


def max_depth(root: Optional[TreeNode]) -> int:
    """
    Returns the maximum depth (height) of a binary tree.
    """

    # Base case: empty tree
    if root is None:
        return 0

    # Recursively get depth of left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # Current node adds 1 to the max of left/right
    return max(left_depth, right_depth) + 1


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Finds the lowest common ancestor (LCA) of two nodes in a BST.
    """

    # If both nodes are smaller, go left
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)

    # If both nodes are larger, go right
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)

    # Otherwise, this node is the LCA
    return root
