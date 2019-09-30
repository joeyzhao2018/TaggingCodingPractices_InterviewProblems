class Solution(object):

    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x==0 and y==0:
            return 0
        from collections import deque
        que=deque()
        que.append((0,0,0))
        visited=set()
        visited.add((0,0))
        x=x if x>0 else -x
        y=y if y>0 else -y
        while que:
            i, j, step=que.popleft()
            # if i==x and j==y:
            #     return step
            for di, dj in [(2, 1), (-2, 1), (2, -1), (-2, -1),(1,2),(-1,2),(1,-2),(-1,-2)]:
                _i, _j=abs(i+di), abs(j+dj)
                if _i==x and  _j==y :
                    return step+1
                if (_i,_j) not in visited:
                    visited.add((_i,_j))
                    que.append((_i,_j,step+1))

s=Solution()
print(s.minKnightMoves(-99,142))