class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)<=1:
            return len(nums)
        from collections import defaultdict
        tally = defaultdict(int)
        for n in nums:
            tally[n] += 1

        totals = defaultdict(int)
        for _, v in tally.items():
            totals[v] += 1

        if self.validate(totals):
            return len(nums)
        pos = len(nums) - 1

        while pos > 2:
            num = nums[pos]
            totals[tally[num]] -= 1
            if totals[tally[num]] == 0:
                del totals[tally[num]]
            tally[num] -= 1
            if tally[num]!=0:
                totals[tally[num]] += 1
            if self.validate(totals):
                return pos
            pos -= 1
        return 2

    def validate(self,totals):
        if len(totals)==1 and ( 1 in totals or 1 in totals.values() ):
            return True
        if len(totals) == 2 and 1 in totals.values():
            k1, k2 = totals.keys()
            if (totals[k1] == 1 and (k1 == k2 + 1 or k1==1)) or (totals[k2] == 1 and (k2 == k1 + 1 or k2==1)):
                return True
        return False
s=Solution()
print(s.maxEqualFreq([1,1,1,1,1,1]))
print(s.maxEqualFreq([2,2,1,1,5,3,3,5]))
print(s.maxEqualFreq([1,2,3,4,5,6,7,8,9]))
print(s.maxEqualFreq([10,10]))
print(s.maxEqualFreq([1,1,1,2,2,2]))
print(s.maxEqualFreq([10,9]))
print(s.maxEqualFreq([10,2,8,9,3,8,1,5,2,3,7,6]))
print(s.maxEqualFreq([1,1,1,2,2,2,3,3,3,4,4,4,5]))
print(s.maxEqualFreq([2,2,1,1,5,3,3,5]))
