class Solution:
    """
    @param s1: A string
    @param s2: Another string
    @return: whether s2 is a scrambled string of s1
    """

    def isScrambleBasicCheck(self, s1, s2):
        # write your code here
        if len(s1) != len(s2):
            return False
        ref = {}
        for i in range(len(s1)):
            ref[s1[i]] = ref.get(s1[i], 0) + 1
            ref[s2[i]] = ref.get(s2[i], 0) - 1

        ans =not any([val for val in ref.values() if val != 0])
        return ans

    def isScramble(self, s1, s2):
        # write your code here
        if not self.isScrambleBasicCheck(s1,s2):
            return False
        n = len(s1)
        dp = [[[False for _ in range(n+1)] for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i][j][1] = True

        for l in range(2, n+1): #length of the section under examination
            for i in range(0, n - l+1): # index of the string can select from 0 to n-l, since s[n-l:n] has length l
                for j in range(0, n - l+1):
                    for k in range(1, l): # further cutting s[i:i+l] into s[i:i+k] and s[i+k:i+l]
                        if (dp[i][j][k] and dp[i + k][j + k][l - k]) \
                                or (dp[i + k][j][l - k] and dp[i][j + l - k][k]):
                            dp[i][j][l] = True
                            break

        return dp[0][0][n]

s=Solution()
print(s.isScramble('great','atgre'))