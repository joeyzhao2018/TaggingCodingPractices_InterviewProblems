description="""You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer."""


class Solution:

    def findTargetSumWays(self, nums, S):
        """
        consider all the + ones as sum1, all the - ones as sum2
        sum1-sum2=S       (1)
        sum1+sum2=total   (2)
        (1)+(2):
        2sum1=S+total
        sum1=(S+total)/2
        Therefore the question is equal to 'finding the number of subset with sum as (S+total)/2'
        """
        if not nums or not len(nums) or S<0:
            return 0
        total=sum(nums)
        target_S=(S+total)//2
        """Important: an optimization"""
        if total<S or (S+total)%2==1:
            return 0

        return self.count_subsets_recursive(nums,0, target_S)
        # return self.count_subsets_dp(nums, target_S)

    def count_subsets_recursive(self,nums,index,S):
        """
        recursive brute force
        """
        if S==0:
            return 1

        if index==len(nums):
            return 0

        count1=0
        if nums[index]<=S: # include nums[index]
            count1=self.count_subsets_recursive(nums, index+1, S-nums[index])

        count2=self.count_subsets_recursive(nums, index+1, S) #exclude nums[index]

        return count1+count2

    def count_subsets_dp(self, nums, S):
        """
        dynamic programming (it can be further optimized for space complexity with rolling)
        """
        n=len(nums)
        dp=[[0 for _ in range(S+1)] for _ in range(n)]

        for i in range(n):# considering 1st element and targeting 0, there's always 1 (set) => the empty set
            dp[i][0]=1
        # considering 1st element and targeting s, first set to 0 counts
        # for s in range(1, S+1):
        #     dp[0][s]=0
        #except in the case s==nums[0]
        if nums[0]<=S:
            dp[0][nums[0]]=1

        for i in range(1,n):
            for s in range(1,S+1):
                count1=0
                if nums[i]<=s:
                    count1=dp[i-1][s-nums[i]]
                count2=dp[i-1][s]

                dp[i][s]=count1+count2

        return dp[n-1][S]


def main():
    solution=Solution()

    assert solution.findTargetSumWays([1, 1, 2, 3], 1)==3
    assert solution.findTargetSumWays([1, 2, 7, 1], 9)==2


main()