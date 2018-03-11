#!/usr/bin/env python
# -*- coding:utf-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 测试用例跑了48ms超越了100%的Python代码,迷之测试
    def deleteDuplicates(self, head):
        """
        :param head: ListNode
        :return: ListNode
        """
        h = head
        while True:
            print(h.val)
            if h.next:
                h = h.next
            else:
                break
        if head is None:
            return None
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                if cur.next.next is None:
                    cur.next = None
                else:
                    temp = cur.next.next
                    cur.next = temp
            else:
                cur = cur.next

        return head


if __name__ == '__main__':
    l = [1, ]
    head = cur = ListNode(0)
    for i in l:
        cur.next = ListNode(i)
        cur = cur.next
    head = head.next
    so = Solution()
    so.deleteDuplicates(head)
    print("###############")
    while True:
        print(head.val)
        if head.next:
            head = head.next
        else:
            break