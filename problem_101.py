#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return False
        else:
            return self._helper(root.left, root.right)

    def _helper(self, p, q):
        if p is None and q is None:
            return True
        elif (p is None and q) or (p and q is None):
            return False
        else:
            return (p.val == q.val) and self._helper(p.left, q.right) and self._helper(p.right, q.left)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(3)
    root.right.left = TreeNode(4)

    so = Solution()
    print(so.isSymmetric(root))
