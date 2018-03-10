#!/usr/bin/env python
# -*- coding:utf-8 -*-
from cmath import sqrt


class Solution(object):

    def mySqrt(self, x):
        """
        x开平方,要求得到整数部分即可.
        :param x:int
        :return: int
        """
        if x < 0:
            return None
        if x >= 6:
            stop = x // 3
            count = 0
            while True:
                if stop ** 2 <= x < (stop + 1) ** 2:
                    print("count1->", count)
                    return stop
                elif stop ** 2 > x:
                    stop //= 2
                elif stop ** 2 < x:
                    stop += 1
                count += 1

        elif 1 <= x < 4:
            return 1
        elif 4 <= x < 6:
            return 2
        else:
            return 0

    def mySqrt2(self, x):
        if x < 0:
            return None
        start, end = 0, x
        count = 0
        while True:
            count += 1
            mid = (start + end) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                print("count2->", count)
                return mid
            elif mid * mid > x:
                end = mid
            elif mid * mid < x:
                start = mid 


'''
mySqrt()方法是单向的,当通过除以2的方法找到大范围后需要用+1的方法来找到具体的值,从结果看运行效率较低,代码特例较多,不美观;
mySqrt2()双向寻找,浮动区间范围除以2,效率更高,而且代码特例较好,美观.
'''
if __name__ == '__main__':
    x = 100000000
    so = Solution()
    print("old->", so.mySqrt(x))
    print("new->", so.mySqrt2(x))
    print(sqrt(x))
