#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 杨辉三角(帕斯卡三角),以数组形式输出
# 不要被形式所束缚,探寻其中的本质规律就能找到答案.
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = [[1], [1, 1]]
        if numRows == 0:
            return []
        elif 0 < numRows < 3:
            return ret[:numRows]
        else:
            while len(ret) < numRows:
                newRow = [1, ]
                for i in range(len(ret[-1]) - 1):
                    newRow.append(ret[-1][i] + ret[-1][i + 1])
                newRow.append(1)
                # print("### new row", newRow)
                ret.append(newRow)
            return ret[-1]

    def generate2(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        ans = [[1 for i in range(i + 1)] for i in range(numRows)]
        for i in range(1, numRows):
            for j in range(1, i):
                ans[i][j] = ans[i - 1][j] + ans[i - 1][j - 1]
        return ans


if __name__ == '__main__':
    so = Solution()
    print(so.generate(4))
