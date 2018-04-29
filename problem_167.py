#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def twoSum(self, numbers, target):
        """
        时间复杂度,O(N*logN)
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        def binary_search(mlist, start, end, target):
            while end >= start:
                mid = (start + end) // 2
                if mlist[mid] == target:
                    return mid
                elif mlist[mid] > target:
                    end = mid - 1
                elif mlist[mid] < target:
                    start = mid + 1

        for i in range(len(numbers) - 1):
            new_target = target - numbers[i]
            res = binary_search(numbers, i + 1, len(numbers) - 1, new_target)
            if res:
                return i + 1, res + 1

    def twoSum2(self, numbers, target):
        """"
        时间复杂度O(n)
        """
        if numbers:
            start = 0
            end = len(numbers) - 1

            while True:
                if start == end:
                    return
                temp = numbers[start] + numbers[end]
                if temp == target:
                    return start + 1, end + 1
                elif temp > target:
                    end -= 1
                else:
                    start += 1
        pass
if __name__ == '__main__':
    l = [2,7,11,15]
    s = Solution()
    print(s.twoSum2(l, 9))
