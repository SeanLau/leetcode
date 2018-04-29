# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        采用边遍历边判断的方法,实现了功能,但是提交超时
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if headA is None or headB is None:
            return
        cur1 = headA
        while cur1:
            cur2 = headB
            while cur2:
                if cur1 == cur2:
                    return cur1
                else:
                    cur2 = cur2.next
            cur1 = cur1.next
        return

    def getIntersectionNode2(self, headA, headB):
        """
        采用先遍历后判断的逻辑,此种方法把链表的存储优势浪费了,使用庞大的列表,对空间的需求和遍历也是绝大的开支,仍超时
        :param headA:
        :param headB:
        :return:
        """
        listA= []
        if headA is None or headB is None:
            return
        cur1 = headA
        while cur1:
            listA.append(cur1)
            cur1 = cur1.next
        cur2 = headB
        while cur2:
            if cur2 in listA:
                return cur2
            else:
                cur2 = cur2.next

    def getIntersectionNode3(self, headA, headB):
        """
        两个链表,如果能同步遍历,则是寻找共同节点的最好办法.先找到共同长度
        :param headA:
        :param headB:
        :return:
        """
        cur1, cur2 = headA, headB
        len1, len2 = 0, 0
        while cur1 or cur2:
            if cur1:
                len1 += 1
                cur1 = cur1.next
            if cur2:
                len2 += 1
                cur2 = cur2.next
        delta = abs(len1 - len2)
        cur1, cur2 = headA, headB
        if len1 > len2:
            while delta > 0:
                cur1 = cur1.next
                delta -= 1
        elif len2 > len1:
            while delta > 0:
                cur2 = cur2.next
                delta -= 1
        while cur1 and cur2:
            if cur1 == cur2:
                return cur1
            cur1 = cur1.next
            cur2 = cur2.next

    def getIntersectionNode4(self, headA, headB):
        """
        车轮战的方式匹配,这种匹配判断逻辑统一,没有程序跳转的过程,用时在提交代码中最短,代码也相对简洁
        cur1 = headA + headB
        cur2 = headB + headA
        这样两者的长度就想相同了,next的步调也是一直的.妙!
        :param headA:
        :param headB:
        :return:
        """
        cur1, cur2 = headA, headB
        while cur1 and cur2 and cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
            if cur1 is None:
                cur1 = headB
            if cur2 is None:
                cur2 = headA
            if cur1 == cur2:
                return cur1


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(3)
    c = ListNode(4)
    d = ListNode(5)
    e = ListNode(6)
    f = ListNode(7)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    A = ListNode(100)
    B = ListNode(200)
    A.next = B
    B.next = c

    s = Solution()
    print(s.getIntersectionNode3(a, A).val)