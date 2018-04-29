#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 判断是否为深度平衡二叉树
# 定义:任意节点,其左子树与右子树深度差值不能大于1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def depthOfTree(r):
            if r:
                result = []
                result.append([r])
                level = 0
                while True:
                    level_count = 0
                    temp = []
                    for i in result[level]:
                        if i.left:
                            temp.append(i.left)
                        if i.right:
                            temp.append(i.right)
                        if i.right is None and i.left is None:
                            level_count += 1
                    if level_count == len(result[level]):
                        break
                    else:
                        result.append(temp)
                        level += 1
                return len(result)
            else:
                return 0

        if not root:
            return True

        return (abs(depthOfTree(root.left) - depthOfTree(root.right)) < 2) and \
               self.isBalanced(root.right) and \
               self.isBalanced(root.left)

    def isBalanced2(self, root):
        def helper(root):
            if root is None:
                return 0
            leftChild = helper(root.left)
            if (leftChild == -1):
                return -1
            rightChild = helper(root.right)
            if (rightChild == -1):
                return -1
            if (abs(leftChild - rightChild) > 1):
                return -1
            return (max(leftChild, rightChild) + 1)

        return (helper(root) != -1)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    # root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    # root.right.right = TreeNode(3)
    # root.right.left = TreeNode(4)

    so = Solution()
    # root = so.isBalanced(root)

    print(so.isBalanced2(root))
