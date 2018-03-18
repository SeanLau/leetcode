#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
验证两个二叉树是否相同
'''
class TreeNode(object):
    def __init__(self):
        self,val = x
        self.left = None
        self.right = None


class Solution(object):
    # 迭代法
    def isSameTree2(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree2(p.left, q.left) and self.isSameTree2(p.right, q.right)


if __name__ == '__main__':
    pass

