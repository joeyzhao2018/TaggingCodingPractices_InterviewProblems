class Solution:
    """
    dp[i][j] is the sub game : nums[i] nums[j] are unbreakable, constraining the sub problem to i+1,...,j-1 balloons
    """

    def maxCoins(self, nums):
        # write your code here
        n = len(nums)+2
        balloons=[1 for _ in range(n)]
        for i in range(n-2):
            balloons[1+i]=nums[i]
        dp = [[0 for _ in range(n)] for _ in range(n)]

        # for i in range(n):
        #     dp[i][i+1] = 0 #because if we hold i and i+1 unbreakable, then there's nothing to break

        for l in range(3, n+1): #the length of the 'holding zone', at least 3 because 2 would get dp[i][i+1] = 0
            for i in range(n-l+1):
                j=i+l-1
                for k in range(i+1,j):
                    dp[i][j]=max(dp[i][j],dp[i][k]+dp[k][j]+balloons[i]*balloons[k]*balloons[j])
        return dp[0][n-1]


    def maxCoins_original(self, nums):
        # write your code here
        n = len(nums)
        dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

        dp[0][0] = dp[n+1][n+1] = 1
        nums.append(1)
        for i in range(n):
            pos = i + 1
            dp[pos][pos] = nums[i-1]*nums[i]*nums[i+1]

        for i in range(n - 2, -1, -1):
            pos_i=i+1
            for j in range(pos_i, n):
                pos_j=j+1
                # first consider popping i last and popping j last
                dp[pos_i][pos_j] = max(nums[i - 1] * nums[j + 1] * nums[i] + dp[pos_i + 1][pos_j],
                                       nums[i - 1] * nums[j + 1] * nums[j] + dp[pos_i][pos_j - 1])

                for k in range(i + 1, j): # popping k last
                    pos_k=k+1
                    val = nums[i - 1] * nums[j + 1] * nums[k] + dp[pos_i][pos_k - 1] + dp[pos_k+1][pos_j]
                    dp[pos_i][pos_j] = max(dp[pos_i][pos_j], val)

        return dp[1][n]

s=Solution()
print(s.maxCoins([4,1,5,10]))