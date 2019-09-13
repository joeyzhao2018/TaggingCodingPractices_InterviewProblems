description="""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

"""

from math import inf

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins or not len(coins) or amount<0:
            return 0
        #ans= self.coin_change_recursive(coins, amount, 0)
        ans= self.coin_change_dp(coins,amount)
        if ans==inf:
            return -1
        return ans

    def coin_change_recursive(self,coins, amount, index):
        if amount==0:
            return 0
        if index>=len(coins):
            return inf
        count1=inf
        if coins[index]<=amount:
            count1=1+self.coin_change_recursive(coins, amount-coins[index],index) #note: same index
        count2=self.coin_change_recursive(coins, amount, index+1) #didn't pick
        return min(count1, count2)

    def coin_change_dp(self, coins, amount):
        """
        two mind traps:
        1. dp[i][j]'s i means the subset coins[:i] , not just coin[i]. So, dp[i-1][j] is indeed the solution for j
            before considering coins[i]
        2. thinking about picking coins[i] twice or more? Wrong! dp[i][j-coins[i]] is on the same row and solving
            that for you. Think ONLY ONE STEP => adding one coins[i]
        """
        n=len(coins)
        dp=[[inf for _ in range(amount+1)] for _ in range(n)]

        for i in range(n):
            dp[i][0]=0  # the ask is regarding the number of coins, not the number of combinations

        for j in range(1,amount//coins[0]+1):
            dp[0][coins[0]*j]=j

        for i in range(1,n):
            for j in range(1,amount+1):
                dp[i][j]=dp[i-1][j]
                if coins[i]<=j:
                    dp[i][j]=min(dp[i][j], 1+ dp[i][j-coins[i]])

        return dp[n-1][amount]




def main():
    solution=Solution()
    print(solution.coinChange([1, 2, 3], 5))
    print(solution.coinChange([1, 2, 3], 11))
    print(solution.coinChange([1, 2, 3], 7))
    print(solution.coinChange([3, 5], 7))
main()