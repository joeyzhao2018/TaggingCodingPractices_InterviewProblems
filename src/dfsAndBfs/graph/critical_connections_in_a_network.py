description="""
Tarjan's bridge-finding algorithm 

 Imagine standing at any node, you first update your idx and low by the step
 "my index is x, and the lowest i can get without going back to my previous is x (so far i know)"
 then you ask all the node you can reach : 
 "what's the lowest idx you can reach without passing me?"
 then you can update your lowest, and report back to your previous node.
 
 In this way, when you find that some node you asked can only reach nodes with idx larger than you
 you are then the only 'gate' for that node to get to all nodes whose idx<=your idx
 your edge to it becomes a critical 'bridge'!
 
 when you ask your adjacent node and find it's visited, then your edge to it is definitely not a bridge.
 because someone else can reach it without going through you.
"""

class Graph(object):
    def __init__(self):
        self.next={}
        self.visited={}
        self.low={}
        self.idx={}
        self.ans=[]
        self.step=0

    def addEdge(self,u,v):
        self.next[u]=self.next.get(u,[])
        self.next[v]=self.next.get(v,[])
        self.next[u].append(v)
        self.next[v].append(u)
        self.visited[u]=0
        self.visited[v]=0

    def lowestIdxCanReachWithoutPrev(self, u, prev):
        self.visited[u]=1
        self.idx[u]=self.low[u]=self.step
        self.step+=1
        for v in self.next[u]:
            if v==prev:
                continue # without going back to prev

            if not self.visited[v]: # never visited?
                self.lowestIdxCanReachWithoutPrev(v, u) # then visit it
                if self.low[v] > self.idx[u]: # and only here you need to worry about if you find a bridge
                    self.ans.append([u,v])
            # now the node v should know the lowest it can reach
            self.low[u]=min(self.low[u],self.low[v])


class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        g=Graph()
        for u, v in connections:
            g.addEdge(u, v)

        g.lowestIdxCanReachWithoutPrev(g.next.keys()[0],-1)
        return g.ans


