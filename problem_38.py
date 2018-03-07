#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 38 count and say


class Solution(object):
    def countAndSay(self, n):
        '''
        :type n: int
        :return: str
        '''
        if n == 1:
            return "1"
        elif n < 1:
            return None
        else:
            cs = self.countAndSay(n - 1)
            temp = cs[0]
            count = 0
            res = ''
            for i in range(len(cs)):
                if cs[i] == temp:
                    count += 1
                else:
                    res += "%s%s" % (count, temp)
                    temp = cs[i]
                    count = 1
            else:
                res += "%s%s" % (count, temp)
            return res

if __name__ == '__main__':

    so = Solution()

    for i in range(1, 10):
        print(so.countAndSay(i))
