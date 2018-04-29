#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Sean Lau'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        root = n = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            carry, val = divmod(val1+val2+carry, 10)  # 这里使用到了val1和val2的值，但之后并未处理val1和val2
            n.next = ListNode(val)
            n = n.next
            print("in loop! ", l1, l2, carry)
        return root.next

l1 = ListNode(5)
l1.next = None
l2 = ListNode(5)
l2.next = None


s = Solution()
ret = s.addTwoNumbers(l1, l2)

