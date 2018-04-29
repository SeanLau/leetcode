#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        temp = n
        foo = []
        mode = 26
        idx_A = 64
        while temp > 0:
            res = temp % mode
            temp //= mode
            if res == 0:
                foo.append(ord("Z"))
                temp -= 1
            else:
                foo.append(res + idx_A)
        foo.reverse()
        return "".join(map(chr, foo))

    def convertToTitle2(self, n):
        letters = [chr(x) for x in range(ord("A"), ord("Z") + 1)]
        foo = []
        while n > 0:
            foo.append(letters[(n - 1) % 26])
            n = (n - 1) // 26
        foo.reverse()
        return "".join(foo)


if __name__ == '__main__':
    s = Solution()
    for i in range(1, 678):
        print(s.convertToTitle2(i))
    # print(s.convertToTitle(26))
