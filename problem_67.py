#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Solution(object):

    def addBinary(self, a, b):
        '''
        :param a: str
        :param b: str
        :return: str
        '''
        if set(a) == set(b) == {"0"}:
            return "0"
        if len(a) < len(b):
            a, b = b, a
        b = b.rjust(len(a), "0")
        print(a)
        print(b)
        res = ["0"] * len(a)
        foo = 0
        for i in range(1, len(a)+1):
            temp = int(a[0-i]) + int(b[0-i])
            if temp + foo == 2:
                foo = 1
                res[0-i] = "0"
            elif temp + foo == 1:
                foo = 0
                res[0-i] = "1"
            elif temp + foo == 0:
                foo = 0
                res[0-i] = "0"
            elif temp + foo == 3:
                foo = 1
                res[0-i] = "1"
        if res[0] == "0" or foo == 1:
            res.insert(0, "1")
        print(res)
        return "".join(res)


if __name__ == '__main__':
    a = "1111"
    b = "1111"
    s = Solution()
    s.addBinary(a, b)
