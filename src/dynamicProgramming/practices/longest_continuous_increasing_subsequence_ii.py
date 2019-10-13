class Solution:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """

    def longestContinuousIncreasingSubsequence2_to_1(self, matrix):
        """
        Matrix doesn't have to be 2 dimension, it can be casted down to 1 dimension array by many methods
        here the method is matrix[i][j]:val --> (val,i,j)
        """
        if not matrix or len(matrix) < 1:
            return 0

        matrix_arr=[]
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                matrix_arr.append(( matrix[i][j], i,j)) #matrix[i][j]:val --> (val,i,j)

        key=lambda  x,y:str(x)+'|'+str(y)
        matrix_arr.sort()
        map_ij_len={}
        directions = [-1, 0, 1, 0]
        ans=1
        for val, x, y in matrix_arr:
            key_xy=key(x,y)
            map_ij_len[key_xy]=map_ij_len.get(key_xy,1)
            for d in range(4):
                x_new, y_new = x + directions[d], y + directions[d - 1]
                if -1 < x_new < m and -1 < y_new < n and matrix[x_new][y_new] < val:
                    map_ij_len[key_xy]=max(map_ij_len[key_xy],map_ij_len.get(key(x_new,y_new),1)+1)
                    ans=max(ans, map_ij_len[key_xy])

        return ans




    def longestContinuousIncreasingSubsequence2(self, matrix):
        if not matrix or len(matrix) < 1:
            return 0
        # write your code here
        self.m = len(matrix)
        self.n = len(matrix[0])

        dp = [[-1 for _ in range(self.n)] for _ in range(self.m)]

        from collections import deque

        myque = deque()

        myque.append((0, 0, 1))
        ans = [1]

        for i in range(self.m):
            for j in range(self.n):
                if dp[i][j] == -1:
                    self.recursive(matrix, dp, i, j, ans)
        return ans[0]

    def recursive(self, matrix, dp, x, y, ans):
        directions = [-1, 0, 1, 0]
        dp[x][y] = 1
        for d in range(4):
            x_new, y_new = x + directions[d], y + directions[d - 1]
            if -1 < x_new < self.m and -1 < y_new < self.n:
                if matrix[x_new][y_new] < matrix[x][y]:
                    dp[x][y] = max(dp[x][y], 1+self.recursive(matrix, dp, x_new, y_new, ans))
        if dp[x][y] > ans[0]:
            ans[0] = dp[x][y]
        return dp[x][y]

s=Solution()
test=[[1,2,3,4,5],[16,17,24,23,6],[15,18,25,22,7],[14,19,20,21,8],[13,12,11,10,9]]
ans=s.longestContinuousIncreasingSubsequence2_to_1(test)
print(ans)