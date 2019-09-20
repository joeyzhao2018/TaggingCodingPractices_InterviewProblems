class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordset = set(wordDict)

        self.lookup = {}

        n = len(s)
        """ 
        
        for i in range(n-1, -1, -1):
             if s[i:] in wordset:
                 self.lookup[s[i:]]=[s[i:]]
             for j in range(n-1, i, -1):
                 if s[i:j] in wordset and s[j:] in self.lookup:
                     self.lookup[s[i:]]=self.lookup.get(s[i:],[])
                     for combo in self.lookup[s[j:]]:
                         self.lookup[s[i:]].append(s[i:j]+' '+combo)
        return self.get(s[0:],[])
        
        this is the same logic as below, but this way it uses too much memory,
        so instead of using self.lookup=Map<theWord, itsPossibleBreakdowns>
        we can use self.lookup as Map<index, nextIndexItCanJumpto>
        
        """
        for i in range(n - 1, -1, -1):
            if s[i:] in wordset:
                self.lookup[i] = [n]
            for j in range(n - 1, i, -1):
                if s[i:j] in wordset and j in self.lookup:
                    self.lookup[i] = self.lookup.get(i, [])
                    # for combo in self.lookup[j]:
                    self.lookup[i].append(j)
        if 0 in self.lookup:
            print(self.lookup)
            self.ans = []
            self.buildWord('', 0, s)
            return self.ans

        return []

    def buildWord(self, currentStr, i, s):

        if i == len(s):
            self.ans.append(currentStr.lstrip())
            return

        for nexti in self.lookup[i]:
            newStr = currentStr + ' ' + s[i:nexti]
            self.buildWord(newStr, nexti, s)