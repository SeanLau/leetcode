#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        foo = "{0:032b}".format(n)
        # foo = bin(n)
        return foo.count("1")

    def hammingWeight2(self, n):
        """最优方法,采用位运算,空间利用率最高"""
        count = 0
        while n > 0:
            if n & 1:
                count += 1
            n >>= 1
        return count


if __name__ == '__main__':
    n = 7
    s = Solution()
    print(s.hammingWeight(n))