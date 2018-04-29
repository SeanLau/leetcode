#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Sean Lau'



class Solution(object):


    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        abcdefb
        """
        longest = 0
        foo = []
        start = 0
        stop = False
        while not stop:
            for c in s[start:]:
                if c not in foo:
                    foo.append(c)
                else:
                    start += s[start:].index(c) + 1
                    break
            print(foo, "start=", start)
            if len(foo) > longest:
                longest = len(foo)
            foo.clear()
            if len(s) - start - 1 < longest:
                stop = True
        return longest

    def lengthOfLongestSubstring(self, s):
        '''
        :type s: str
        :return: int
        执行速度有所提升，通过。
        '''
        if not s:
            return 0
        sub = {}
        lengthList = set()
        longest = 0
        startIdx = 0
        for i in range(len(s)):
            if s[i] in sub.keys():
                if sub[s[i]] + 1 > startIdx:
                    startIdx = sub[s[i]] + 1
            sub[s[i]] = i
            longest = i - startIdx + 1
            lengthList.add(longest)
            print(sub, startIdx, longest)

        return max(lengthList)


ts = "aaabbcca"
s = Solution()
print(s.lengthOfLongestSubstring(ts))