from math import inf
class Solution:
    def makeArrayIncreasing(self, arr1, arr2) :
        arr2.sort()
        memo={}
        ans= self.makeIncreasingRecursive(memo, arr1, arr2, -1, 0, 0)
        if ans is inf:
            return -1
        return ans

    def makeIncreasingRecursive(self,memo, arr1, arr2, prev, i_1, i_2):
        key= str(i_1)+'|'+str(i_2)+'|'+str(prev)
        if key in memo:
            return memo[key]
        memo[key]=inf
        if i_1==len(arr1):
            return 0
        if arr1[i_1] > prev:
            memo[key]=min(memo[key], self.makeIncreasingRecursive(memo, arr1, arr2, arr1[i_1], i_1 + 1, i_2))

        while i_2 < len(arr2) and arr2[i_2] <= prev:
            i_2 += 1
        if i_2 < len(arr2):
            memo[key] = min(memo[key],1+self.makeIncreasingRecursive(memo, arr1, arr2, arr2[i_2], i_1 + 1, i_2 + 1))

        return memo[key]

s=Solution()

print(s.makeArrayIncreasing([1,5,3,6,7],[1,3,2,4]))