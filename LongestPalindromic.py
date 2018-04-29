#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Sean Lau'


class Solution:
    def longestPalindrome1(self, s):
        '''
        最长回文字符串
        :param s: 
        :return: palindrome
        '''
        # 思路从第1位步进，做为中心判断回文字符串
        retList = {}
        if len(s) == 1:
            return s
        for i in range(1, len(s)):
            j = 0
            for j in range(i+1):
                if (i+j > len(s)-1) or (s[i+j] != s[i-1-j]):
                    break
            if j - 1 >= 0:
                retList[2*j] = (i-j, i+j)
            j = 0
            for j in range(i+1):
                if (i+j+1 > len(s)-1) or (s[i+j+1] != s[i-1-j]):
                    break
            if j - 1 >= 0:
                retList[2*j+1] = (i-j, i+j+1)
            if (2*j+1 == len(s)) or (2j == len(s)):
                break
        if len(retList):
            b, e = retList[max(retList.keys())]
            return s[b: e]
        else:
            return s[0]


    def longestPalindrome(self, s):
        '''
        最长回文字符串
        :param s: 
        :return: palindrome
        '''
        # 思路从第1位步进，做为中心判断回文字符串
        ret = (0, 0)
        if len(s) == 1:
            return s
        for i in range(1, len(s)):
            j = 0
            for j in range(i+1):
                if (i+j > len(s)-1) or (s[i+j] != s[i-1-j]):
                    break
            if j - 1 >= 0:
                if 2*j > (ret[1] - ret[0]):
                    ret = (i-j, i+j)
            j = 0
            for j in range(i+1):
                if (i+j+1 > len(s)-1) or (s[i+j+1] != s[i-1-j]):
                    break
            if j - 1 >= 0:
                if 2*j+1 > (ret[1] - ret[0]):
                    ret = (i-j, i+j+1)
            if (2*j+1 == len(s)) or (2j == len(s)):
                break
        if (ret[1] - ret[0]) != 0:
            return s[ret[0]: ret[1]]
        else:
            return s[0]

s = Solution()
st = "abcda"
print(s.longestPalindrome(st))