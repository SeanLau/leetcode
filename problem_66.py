#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Solution(object):
    def plusOne(self, digits):
        '''
        两种方法均可,在验证中第一种方法,运行效率比第二种好
        :param digits: list[int
        :return: list[int
        '''
        total = 0
        for i in digits:
            total = total * 10 + i
        print(total)
        total += 1
        digits = []
        while total != 0:
            digits.insert(0, (total % 10))
            total //= 10
        print(digits)
        return digits

    # 注意range参数(len(digits)-1, -1, -1)表示逆序遍历,第二个"-1"并不是表示对应列表的索引位置,这点误区要改正!
    # 其分别对应起始点,终止点(不包括此值),step
    def plusOne2(self, digits):

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                break
            digits[0]
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    di = [1, 3, 9]
    s = Solution()
    print(s.plusOne(di))

    for i in range(len(di) - 1, -1, -1):
        print(i)
