from collections import defaultdict, deque
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        n=len(endWord)
        wordList=[w for w in wordList if len(w)==n]

        adjacent = defaultdict(list)
        for w in wordList:
            for i in range(n):
                k = w[:i] + '*' + w[i+1:]
                adjacent[k].append(w)

        wordList.append(beginWord)

        ans=[]
        queue=deque()
        queue.append((beginWord,[beginWord]))
        visited = {beginWord:0}
        while queue:
            currWord,path=queue.popleft()
            lookuplist=[]
            for i in range(n):
                k = currWord[:i] + '*' + currWord[i + 1:]
                lookuplist+=adjacent[k]
            for w in lookuplist:
                if (w not in visited or visited[w]>len(path)):
                    newpath=path[:]
                    newpath.append(w)
                    if w==endWord:
                        if len(ans) and len(ans[0])<len(newpath):
                            return ans
                        ans.append(newpath)
                    else:
                        visited[w]=len(newpath)
                        queue.append((w,newpath))
        return ans




# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# beginWord = "a"
# endWord = "c"
# wordList = ["a","b","c"]

beginWord ="red"
endWord = "tax"
wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
s=Solution()

ans=s.findLadders(beginWord,endWord,wordList)
print(ans)