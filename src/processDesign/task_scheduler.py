description="""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.
However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.
You need to return the least number of intervals the CPU will take to finish all the given tasks.

Input: tasks = ['A','A','A','B','B','B'], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B.
"""
# there's a greedy algorithm solution: ans = max(len(tasks), (longest - 1) * (n + 1) + counts.count(longest) )
# but here the important thing is to simulate it

class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """

    def leastInterval(self, tasks, n):
        # write your code here
        import heapq

        class Task(object):
            def __init__(self, name, cooldown, total):
                self.name = name
                self.cooldown = cooldown
                self.total = total

            def __lt__(self, another):  # which is more important
                return self.total > another.total

        myhash = {}
        for t in tasks:
            myhash[t] = myhash.get(t, 0)
            myhash[t] += 1

        heap = [] # heap items are all 'READY' tasks, it will pop the task with max 'total times (left) to run'
        for t, count in myhash.items():
            heapq.heappush(heap, Task(t, 0, count))

        from collections import deque
        waitqueue = deque() # waitqueue is for 'COOLING' tasks, it's an increasing list regarding cooldown

        curr_time = 0

        while heap or waitqueue:
            curr_time += 1
            while waitqueue and waitqueue[0].cooldown <= curr_time:
                waitqueue[0].cooldown = 0
                heapq.heappush(heap, waitqueue.popleft())
            if heap:
                next_task = heapq.heappop(heap)
                print([curr_time, next_task.name])

                if next_task.total > 1:
                    waitqueue.append(Task(next_task.name, curr_time + n + 1, next_task.total - 1))
                # heapq.heappush(heap,Task(next_task.name, curr_time+n+1,next_task.total-1))
        return curr_time