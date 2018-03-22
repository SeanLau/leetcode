#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 二叉树遍历，按层输出

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root:
            result = []
            result.append([root])
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
            ret = []
            for i in result:
                foo = []
                for j in i:
                    foo.append(j.val)
                ret.insert(0, foo)
            return ret
        else:
            return []

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(3)
    root.right.left = TreeNode(4)

    so = Solution()
    print(so.levelOrderBottom(root))