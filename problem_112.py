#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        :desc: 此解法的问题在于,修改了节点的值,并且把每种结果都计算出来
        """
        if not root: return False
        nodes_list = [root, ]  # 节点列表

        while True:
            temple = []
            level_value = []  # 层值列表
            for node in nodes_list:

                if node.left:
                    temple.append(node.left)
                    new_val = node.val + node.left.val
                    node.left.val = new_val
                    level_value.append(new_val)

                if node.right:
                    temple.append(node.right)
                    new_val = node.val + node.right.val
                    node.right.val = new_val
                    level_value.append(new_val)

                if node.left is None and node.right is None:
                    temple.append(node)
                    level_value.append(node.val)
            nodes_list = temple
            for i in nodes_list:
                if i.right or i.left:
                    break
            else:
                break
        print("Final values ==", level_value)
        if sum in level_value:
            return True
        else:
            return False

    def hasPathSum2(self, root, sum):
        """
        此方法无需修改节点值,仅仅从传入sum参数下手,通过迭代完成了值的检测,弥补了原方法的不足,提高了一定效率.
        :param root:
        :param sum:
        :return:
        """
        if not root:
            return False

        if root.val == sum:
            if root.left is None and root.right is None:
                return True
            else:
                return self.hasPathSum2(root.left, sum - root.val) or self.hasPathSum2(root.right, sum - root.val)
        return self.hasPathSum2(root.left, sum - root.val) or self.hasPathSum2(root.right, sum - root.val)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    # root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    # root.right.right = TreeNode(3)
    root.right.left = TreeNode(4)

    so = Solution()
    print(so.hasPathSum(root, 6))
