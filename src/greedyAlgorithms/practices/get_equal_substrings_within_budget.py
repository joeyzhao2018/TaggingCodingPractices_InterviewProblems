class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        n=len(s)
        start=0
        end=0
        currCost=0
        ans=0
        diff=[abs(ord(s[i])-ord(t[i])) for i in range(n)]
        while end<n and start+ans<n:
            end+=1
            currCost+=diff[end-1]
            if currCost<=maxCost:
                ans=max(ans, end-start)
            while currCost>maxCost:
                currCost-=diff[start]
                start+=1
        return ans




s=Solution()

print(s.equalSubstring("krrgw","zjxss",19))
print(s.equalSubstring("abcd","bcdf",3))