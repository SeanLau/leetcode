#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Sean Lau'

"""
中位数，数组个数为奇数时，取中间那个；个数为偶数时取中间两个的平均数。
"""


class Solution:


    def findMedianSortedArrays(self, nums1, nums2):
        '''
        :param nums1: List[int]
        :param nums2: List[int]
        :return: float
        '''
        m = len(nums1)
        n = len(nums2)
        newNums = []
        # 确定列表顺序
        if nums1[-1] < nums1[0]:
            nums1 = sorted(nums1, reverse=True)
        if nums2[-1] < nums2[0]:
            nums2 = sorted(nums2, reverse=True)
        # 两数组区间无重叠,通过索引找
        if nums1[-1] <= nums2[0]:
            newNums = nums1 + nums2
        elif nums1[0] >= nums2[-1]:
            newNums = nums2 + nums1
            print(newNums)
        else:  # 有交集
            # 找出交集部分
            if nums2[-1] > nums1[0]:
                nums1, nums2 = (nums2, nums1)

            stop1 = 0
            stop2 = 0
            for i in range(len(nums2)):
                if nums2[i] > nums1[-1]:
                    stop2 = i
                    break
            for j in range(len(nums1)):
                if nums1[j] > nums2[0]:
                    stop1 = j
                    break
            nums1[stop1:]
            nums2[0: stop2]
            # 交集排序 nums1[stop1:],nums2[0:stop2]
            foo = 0
            i = stop1
            j = 0
            fooList = []
            while True:
                if nums1[i] - foo < nums2[j] - foo:
                    foo = nums1[i]
                    i += 1
                else:
                    foo = nums2[j]
                    j += 1
                fooList.append(foo)
                if i >= len(nums1) and j <= len(nums2):
                    fooList.extend(nums2[j:])
                    break
                elif j >= len(nums2) and i <= len(nums1):
                    fooList.extend(nums1[i:])
                    break
                elif j >= len(nums2) and i >= len(nums1):
                    break
            # 找中位数
            newNums = nums1[0: stop1] + fooList + nums2[stop2: ]

        if (m + n) % 2 == 0:
            return (newNums[(m + n)/2] + newNums[(m + n)/2-1]) / 2
        else:
            return newNums[(m + n - 1)//2]

s = Solution()

l1 = [1, 3, 5, 7, 10, 11, 22, 23, 23, 25, 28]
l2 = [28, 29, 30, 31]

print(s.findMedianSortedArrays(l1, l2))
