#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Sean Lau'


class Solution:
    def myAtoi(self, s):
        s = s.strip()
        if s == "+" or s == "-" or len(s) == 0:
            return 0
        else:
            foo = ""
            for i in s:
                if i == "+" or i == "-" or i.isnumeric():
                    foo += i
                else:
                    break

            mCount = foo.count("-")
            pCount = foo.count("+")
            foo = foo.replace("-", "", len(foo))
            foo = foo.replace("+", "", len(foo))
            if mCount + pCount > 1:
                return 0
            # print(foo)
            if foo.isdigit():
                res = int(foo, base=10)
            else:
                res = 0

            if mCount % 2:
                return 0 - res if res <= 2**31 else 0 - 2**31
            else:
                return res if res <= 2**31 - 1 else 2**31 - 1


s = Solution()
a = "-2147483648"
print(a.isnumeric())
print(s.myAtoi(a))