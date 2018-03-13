#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2
        else:
            idx = 0 - m
            for i in nums2:
                while idx <= -2:
                    if nums1[idx + 1] > i >= nums1[idx]:
                        nums1.insert(idx + 1, i)
                        break
                    elif i < nums1[0 - m]:
                        nums1.insert(0, i)
                        break
                    elif i > nums1[-1]:
                        nums1.append(i)
                        break
                    else:
                        idx += 1
                        continue
                else:
                    if i >= nums1[0]:
                        nums1.append(i)
                    else:
                        nums1.insert(-1, i)
        print("nums1->", nums1)

    # 代码效率凭运气,merge2有时处于中游,有时处于顶端
    def merge2(self, nums1, m, nums2, n):
        nums1[m:] = nums2[:n]
        nums1.sort()

    # 此方法利用了空间的逆向思路,从大端开始比较,从而减少了时间复杂度.该代码多次验证,效率均很稳健.
    def merge3(self, nums1, m, nums2, n):
        cur_index = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 or n >= 0:
            if m < 0:
                nums1[cur_index] = nums2[n]
                cur_index -= 1
                n -= 1
                continue
            if n < 0:
                nums1[cur_index] = nums1[m]
                cur_index -= 1
                m -= 1
                continue
            if m >= 0 and n >= 0:
                if nums1[m] >= nums2[n]:
                    nums1[cur_index] = nums1[m]
                    cur_index -= 1
                    m -= 1
                    continue
                else:
                    nums1[cur_index] = nums2[n]
                    cur_index -= 1
                    n -= 1


'''
# 这是否揭示了Python的一个Bug?:
if m == 0:
    nums1 = nums2
# nums1在函数内部得到了复制,但实际参数对象并未改变.
# 而使用.extend()函数则能够引起nums1对应实际参数对象的改变
    nums1.extend()  # it work
# 这并不是一个BUG,而是对Python变量定义认识不清造成的.
变量出现在等号的左侧就是从新定义了一个变量,不是引用已有的变量!
'''

if __name__ == '__main__':
    l1 = [0]
    l2 = [11, 12]
    so = Solution()
    print(sorted(l1 + l2))
    so.merge(l1, len(l1), l2, len(l2))
    print(l1)
