#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k:
            nums.insert(0, nums[-1])
            nums.pop()
            k -= 1

    def rotate2(self, nums, k):
        foo = nums[- k:]
        print(foo)
        for i in range(-k-1, -len(nums)-1, -1):
            nums[i + k] = nums[i]
        nums[0:k] = foo

    def rotate3(self, nums, k):
        length = len(nums)
        if k <= 0:
            return
        elif 0 < k < length:
            nums[0:k], nums[k:length] = nums[length - k: length], nums[0:length - k]
        elif k > length:
            k = k - length
            nums[0:k], nums[k:length] = nums[length - k: length], nums[0:length - k]




if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6]
    print(l[-1: -5])
    s = Solution()
    s.rotate3(l, 3)
    print(l)
