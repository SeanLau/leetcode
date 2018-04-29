#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 寻找最短深度
# 思路1,逐层遍历即可寻找到最短路径.

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            result = []  # 存储列表的列表
            result.append([root])
            level = 0
            while True:
                temp = []
                for i in result[level]:
                    if i.left:
                        temp.append(i.left)
                    if i.right:
                        temp.append(i.right)
                    if i.right is None and i.left is None:
                        return level + 1
                result.append(temp)
                level += 1
        else:
            return 0

    def minDepth2(self, root):
        if not root: return 0
        depth = 1
        bfs = deque([root])
        while bfs:
            for i in range(len(bfs)):
                node = bfs.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left: bfs.append(node.left)
                if node.right: bfs.append(node.right)
            depth += 1


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(3)
    root.right.left = TreeNode(4)

    so = Solution()
    print(so.minDepth(root))