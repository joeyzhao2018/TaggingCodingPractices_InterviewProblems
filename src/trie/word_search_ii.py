description="""
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally 
or vertically neighboring. The same letter cell may not be used more than once in a word.
Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
"""


class TrieNode(object):
    def __init__(self,char=None):
        self.char=char
        self.is_word=False
        self.children={}

    def addWord(self,word,i=0):
        if word[i] not in self.children:
            self.children[word[i]] = TrieNode(word[i])
        if i==len(word)-1:
            self.children[word[i]].is_word=True
            self.children[word[i]].word=word # record the full word
        else:
            self.children[word[i]].addWord(word, i + 1)

    # def findWord(self,word)


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie=TrieNode()
        for word in words:
            trie.addWord(word)

        visited=set()
        m=len(board)
        n=len(board[0])
        ans=set()
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.children:
                    visited.add((i,j))
                    self.find(board, visited, i, j, trie.children[board[i][j]],ans)
                    visited.remove((i,j))
        return list(ans)

    def find(self, board, visited, x, y, trieNode, ans):
        if trieNode.is_word and trieNode.word not in ans:
            ans.add(trieNode.word)


        inBoard=lambda x,y : 0<=x<len(board) and 0<=y<len(board[0])

        for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            _x, _y=x+dx, y+dy
            if inBoard(_x, _y) and (_x,_y) not in visited and  board[_x][_y] in trieNode.children:
                visited.add((_x,_y))
                self.find(board, visited, _x, _y, trieNode.children.get(board[_x][_y]), ans)
                visited.remove((_x,_y))

board=[["a","a"]]
words=["aaa"]
s=Solution()
print(s.findWords(board,words))