# https://youtu.be/pSW8wxvcEcM

class Solution(object):

    def minBuildTime(self, blocks, split):
        """
        always find two smallest time
        then take the larger of the two (which is simply the 2nd heappop result)
        and add split
        we got another block
        this block can be interpreted as
        "if we have these two blocks and one worker, it's equivalent to having one block,
        whose time = split + the larger of the two smallest"


        """
        import heapq
        heap=[]
        for b in blocks:
            heapq.heappush(heap, b)
        while len(heap)>1:
            heapq.heappop(heap)
            y=heapq.heappop(heap)
            heapq.heappush(heap,y+split)
        return heapq.heappop(heap)