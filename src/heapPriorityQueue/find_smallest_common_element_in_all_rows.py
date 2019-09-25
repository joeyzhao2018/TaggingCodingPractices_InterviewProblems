class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        if not mat or len(mat)<1 or len(mat[0])<1:
            return -1

        class Node(object):
            def __init__(self, val):
                self.val = val
                self.list = []

            def add(self, i):
                self.list.append(i)

            def __lt__(self, another):
                return self.val < another.val

        import heapq

        heap = []
        myhash = {}
        n = len(mat)
        for i in range(n):
            if mat[i][0] in myhash:
                myhash[mat[i][0]].add((i, 0))
            else:
                newNode = Node(mat[i][0])
                newNode.add((i, 0))
                myhash[mat[i][0]] = newNode
                heapq.heappush(heap, newNode)

        while len(heap) != 1:
            minNode = heapq.heappop(heap)
            del myhash[minNode.val]
            mylist = minNode.list
            for i, j in mylist:
                if j == len(mat[i]) - 1:
                    return -1
                if mat[i][j + 1] in myhash:
                    myhash[mat[i][j + 1]].add((i, j + 1))
                else:
                    newNode = Node(mat[i][j + 1])
                    newNode.add((i, j + 1))
                    myhash[mat[i][j + 1]] = newNode
                    heapq.heappush(heap, newNode)
        return heap[0].val

t=[[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
s=Solution()

print(s.smallestCommonElement(t))