#!/usr/bin/env python
# -*- coding:utf-8 -*-

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        foo = float("inf")
        self.__m_list = [foo, ]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if type(x) is int:
            if x < self.__m_list[0]:
                self.__m_list[0] = x
            self.__m_list.append(x)
            print("push result:", self.__m_list)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.__m_list) > 2:
            self.__m_list.pop()
            self.__m_list[0] = min(self.__m_list[1:])  # 此处也可以用循环遍历寻找最小,复杂度都是O(n)
        elif len(self.__m_list) == 2:
            self.__m_list.pop()
            self.__m_list[0] = float('inf')
        else:
            return
        print("pop result:", self.__m_list)

    def top(self):
        """
        :rtype: int
        """
        if len(self.__m_list) > 1:
            return self.__m_list[-1]


    def getMin(self):
        """
        :rtype: int
        """
        if len(self.__m_list) > 1:
            return self.__m_list[0]
        else:
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == '__main__':
    m = MinStack()
    m.push(5)
    m.push(2)
    m.pop()
    m.pop()