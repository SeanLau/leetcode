#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):

    def trailingZeroes(self, n):
        """
        两种思路,
        一直接的方法,运算,然后计数.缺点,浪费算力,时间慢
        二分析过程,推演结果,也就是说计算n之前乘过多少个5,利用循环不断剥皮就可以了
        "剥皮算法"
        :param n:
        :return:
        """
        total = 0
        while n >= 5:
            n = n // 5
            total += n
        return total


if __name__ == '__main__':
    s= Solution()
    print(s.trailingZeroes(125))
