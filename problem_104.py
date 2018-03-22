#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 此题可以先序遍历二叉树，找到最长的即可

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        if not root:
            return depth
        result = []

        def preOrder(root, depth):
            # return root
            depth += 1
            if root.left:
                preOrder(root.left, depth)
            if root.right:
                preOrder(root.right, depth)
            # yield depth

            if not (root.left and root.right):
                print("## depth in ===>", depth)
                result.append(depth)

        preOrder(root, depth)

        return max(result)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(3)
    root.right.left = TreeNode(4)

    so = Solution()
    print(so.maxDepth(root))
