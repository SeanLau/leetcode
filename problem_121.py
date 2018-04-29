#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        利用传统方法的逻辑并不复杂,但是面对大量数据时,就会遇到超时的问题.
        """
        income = 0
        for i in range(len(prices) - 1):
            buy = prices[i]
            foo = max(prices[i + 1:]) - buy
            if foo >= income:
                income = foo
        if income < 0:
            return 0
        else:
            return income

    def maxProfit(self, prices):
        '''
        首先确认要什么值,要差值,计算获得最大差值即可.
        确定寻找列表左侧最小值,然后逐步确认对大差值的过程.
        :param prices:
        :return:
        '''
        maxProfit, minPrice = 0,float('inf')  # 正无穷
        for p in prices:
            # if p < minPrice:
            #     minPrice = p
            #     continue
            # maxProfit = max(maxProfit, p - minPrice
            if p > minPrice:
                maxProfit = max(maxProfit, p - minPrice)
            else:
                minPrice = p
        return maxProfit


if __name__ == '__main__':
    ll = [7, 1, 5, 4, 3, 2, 1]
    so = Solution()
    print(so.maxProfit(ll))
