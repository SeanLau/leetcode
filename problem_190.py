#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    """
    这里需要注意的是,切片使用的灵活性.
    """

    def reverseBits(self, n):
        """
        :param n:
        :return:
        """
        foo = bin(n)
        foo_str = str(foo)[2:]
        foo_str = foo_str.rjust(32, "0")
        foo_str = list(foo_str)
        foo_str.reverse()
        return int(eval("0b" + "".join(foo_str)))

    def reverseBits2(self, n):
        s = bin(n)[-1:1:-1]
        s += (32 - len(s)) * "0"
        return int(s, 2)

    def reverseBits3(self, n):
        tmp = "{0:032b}".format(n)
        return int(tmp[::-1], 2)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits3(43261596))