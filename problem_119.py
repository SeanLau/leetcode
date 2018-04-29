class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        O(k^2)
        """
        ret = [[1], [1, 1]]
        if 0 <= rowIndex < 2:
            return ret[rowIndex]
        else:
            while len(ret) < rowIndex + 1:
                newRow = [1, ]
                for i in range(len(ret[-1]) - 1):
                    newRow.append(ret[-1][i] + ret[-1][i + 1])
                newRow.append(1)
                ret.append(newRow)
            return ret[-1]

    def getRow2(self, rowIndex):
        '''
        与getRow时间复杂度相同,只是将运算压缩到了一个列表中完成,节省了生成新列表的内存和时间的开支.
        :param rowIndex:
        :return:
        '''
        ans = [1 for i in range(rowIndex + 1)]
        for i in range(1, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                ans[j] = ans[j - 1] + ans[j]
        return ans


if __name__ == '__main__':
    so = Solution()

    # for i in range(10):
    #     print(so.getRow(i))
