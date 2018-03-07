#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Solution(object):

    def lengthOfLastWord(self, s):
        '''
        :param s: str
        :return int:
        '''
        if s == " ":
            return 0
        temp = s.strip()
        for i in range(1, len(temp)+1):
            if temp[0-i] == " ":
                return i-1
        else:
            return len(temp)


if __name__ == '__main__':
    s = "a "
    so = Solution()
    print(so.lengthOfLastWord(s))
