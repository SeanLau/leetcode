#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        if len(prices) < 2:
            return 0
        for i in range(0, len(prices) - 1):
            if prices[i] < prices[i + 1]:
                total += prices[i + 1] - prices[i]
        return total


if __name__ == '__main__':
    p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 3, 2, 1, 10]
    s = Solution()
    print(s.maxProfit(p))
