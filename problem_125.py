#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

class Solution:
    def isPalindrome(self, s):
        """
        用了太多循环,高级方法效率比这个高
        :type s: str
        :rtype: bool
        """
        if s.strip() == "":
            return True
        idx_left = -1
        idx_right = 0
        while True:
            while idx_left < len(s)-1:
                idx_left += 1
                if not s[idx_left].isalnum():
                    continue
                else:
                    break

            while idx_right >= 1 - len(s):
                idx_right -= 1
                if not s[idx_right].isalnum():
                    continue
                else:
                    break

            if idx_left == len(s) - 1 or idx_right == 0-len(s):
                return True

            if s[idx_left].lower() != s[idx_right].lower():
                return False


    def isPalindrome2(self, s):
        if len(s) < 2:
            return True
        tmp = ""
        for i in s:
            i  = i.lower()
            if i.isalnum():
                tmp = tmp + i
        lens = len(tmp)//2
        if tmp[:lens] == tmp[len(tmp)-1:len(tmp)-lens-1:-1]:
            return True
        else:
            return False


    def isPalindrome3(self, s):
        """
        利用正则提取的方法耗时相对稳定.
        字符串->纯字符串->list->list.reverse()->字符串->比较
        这里用的都是高级的方法,但速度确实最稳定的.
        :param s:
        :return:
        """
        ss = re.sub("\W", "", s.strip())
        if not ss or len(ss) == 1:
            return True
        l = list(ss.lower())
        l.reverse()
        rss = "".join(l)
        if ss.lower() == rss:
            return True
        return False


if __name__ == '__main__':
    s = "....s896"
    so = Solution()
    print(so.isPalindrome2(s))