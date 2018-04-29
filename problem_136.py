#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temple = set()
        for i in nums:
            if i not in temple:
                temple.add(i)
            else:
                temple.remove(i)
        for j in temple:
            return j

    def singleNumber2(self, nums):
        """通过逻辑操作获得"""
        ans = 0
        for num in nums:
            ans ^= num
            print("ans = ", ans)
        return ans

    def singleNumber3(self, nums):
        '''通过算数运算获得'''
        return 2*sum(list(set(nums))) - sum(nums)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 7]
    s = Solution()
    print(s.singleNumber3(nums))
