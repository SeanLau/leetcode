#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 深度平衡二叉树：两个子树的任意节点的深度差值不超过1
# 直白地描述就是按照中序遍历的逆过程构造二叉树



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)
        if length:
            root = TreeNode(nums[length // 2])
            root.left = self.sortedArrayToBST(nums[:length // 2])
            root.right = self.sortedArrayToBST(nums[(length // 2 + 1):])
            return root
        else:
            return None

    def sortedArrayToBST2(self, nums):
        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root
        return build(0, len(nums)-1)

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
    nums = [-10, -3, 0, 5, 9]
    so = Solution()
    root = so.sortedArrayToBST(nums)

    print(so.levelOrderBottom(root))
