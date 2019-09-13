class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        n = len(values)
        dp = [[0 for _ in range(n + 1)] for _ in range(2)]
        # let the difference = Player 1 - Player 2
        dp[0][n] = 0 # dp[0][i] is the difference when player 1 starts to pick from values[i]
        dp[1][n] = 0 # dp[1][i] is the difference when player 2 starts to pick from values[i]
        dp[0][n - 1] = values[n - 1]
        dp[1][n - 1] = -values[n - 1] # when player 2 pick, he wants to minimize the difference
        for i in range(n - 2, -1, -1):
            dp[0][i] = max(values[i] + dp[1][i + 1], values[i] + values[i + 1] + dp[1][i + 2])
            dp[1][i] = min(-values[i] + dp[0][i + 1], -values[i] - values[i + 1] + dp[0][i + 2])

        print(dp)
        return dp[0][0] > 0