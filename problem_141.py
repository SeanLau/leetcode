#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur = head
        list_set = set()
        while cur:
            if cur in list_set:
                return True
            else:
                list_set.add(cur)
                cur = cur.next

        return False

    def hasCycle2(self, head):
        """
        此种方法修改了head.val值,但并没有借助外部变量存储.
        :param head:
        :return:
        """
        TAG = object()
        while head:
            if head.val is TAG:
                return True
            head.val = TAG
            head = head.next
        return False


if __name__ == '__main__':
    root = ListNode(0)
    cur = root
    for i in range(1, 10):
        cur.next = ListNode(i)
        cur = cur.next
    cur.next = root

    s = Solution()
    print(s.hasCycle2(root))
