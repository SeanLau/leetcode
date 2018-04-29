#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        total = 0
        for i in range(1, n + 1):
            total += (26 ** (i - 1)) * (ord(s[0 - i]) - 64)
        print(total)
        return total

    def titleToNumber2(self, s):
        """
        从大到小
        :param s:
        :return:
        """
        total = 0
        for i in range(len(s)):
            total = total * 26 + ord(s[i]) - ord("A") + 1
        print(total)
        return total


if __name__ == '__main__':
    s = Solution()
    s.titleToNumber("A")
    s.titleToNumber2("A")
    s.titleToNumber("AB")
    s.titleToNumber2("AB")
    s.titleToNumber("ABB")
    s.titleToNumber2("ABB")
    s.titleToNumber("AAAA")
    s.titleToNumber2("AAAA")
