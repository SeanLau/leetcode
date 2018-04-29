#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Sean Lau'
'''
给字符串进行Z字形排列，并重新组合字符串
'''

class Solution:
    def convert(self, s, numRows):

        if numRows <= 0:
            return None
        if numRows >= len(s) or numRows == 1:
            return s
        foo = ["" for x in range(numRows)]
        idx = -1
        step = 1
        for si in s:
            idx += step
            if idx == numRows:
                idx -= 2
                step = -1
            elif idx == -1:
                idx += 2
                step = 1
            print("idx ", idx)
            foo[idx] += si
        return "".join(foo)

    def convert2(self, s, numRows):
        if numRows <= 0:
            return None
        foo = [""] * numRows
        idx, step = 0, 1
        for i in s:
            foo[idx] += i
            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1
            idx += step

        return "".join(foo)

s = "PAYPALISHIRING"
sol = Solution()
print(sol.convert2(s, 3))
print("PAHNAPLSIIGYIR")
