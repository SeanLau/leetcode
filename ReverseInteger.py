#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Sean Lau'
class Solution:
    def reverse1(self, x):
        if -2**31 <= x <= 2**31 - 1:
            foo, i, r = abs(x), 0, 0
            while foo != 0:
                foo, i = divmod(foo, 10)
                print("foo=%d, i=%d" % (foo, i))
                r = r * 10 + i
            if -2**31 <= r <= 2**31 - 1:
                return r if x > 0 else 0 - r
            else:
                return 0
        else:
            return 0

    def reverse(self, x):
        foo = str(abs(x))
        foo = foo[::-1]
        foo = int(foo)
        if foo > 2**31-1 or foo < -2**31:
            return 0
        else:
            return foo if x > 0 else 0 - foo
s = Solution()
print(s.reverse(153423))