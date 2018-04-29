#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def majorityElement(self, nums):
        """
        求众数, 时间复杂度为O(n)
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        num_map = {}
        for i in nums:
            if i in num_map.keys():
                num_map[i] += 1
                if num_map[i] > n // 2:
                    return i
            else:
                num_map[i] = 1
        # return num_map

    def majorityElement2(self, nums):
        nums.sort()
        return nums[len(nums) // 2]


if __name__ == '__main__':
    l = [1, 2, 3, 4, 2, 2, 4, 2, 2, 2, 2]
    s = Solution()
    print(s.majorityElement2(l))
