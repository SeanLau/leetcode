#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def climbStairs(self, n):
        """
        :param n: int
        :return: int
        """
        res = {}
        res[1] = 1
        res[2] = 2

        for i in range(3, n + 1):
            res[i] = res[i - 1] + res[i - 2]
        return res[n]

    def climbStairs2(self, n):
        """
        :param n: int
        :return: int
        """
        a = b = 1
        for _ in range(n):
            a, b = b, a + b

        return a

"""
之后的结果与之前的结果相关,类似斐波那契数列的求法,单纯用迭代会造成严重的资源消耗,所以用字典的结构进行了改进,效率有所提升,
方法1,超越了100%的提交代码
方法2,类似,只是不保存中间变量而已,但效果比第一种稍差,但也是十分领先的.
"""
if __name__ == '__main__':
    so = Solution()
    print(so.climbStairs2(36))
