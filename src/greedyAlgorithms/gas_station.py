class Solution:
    """
    Greedy Algorithm
    1. Starting from station i, if at station j gasLeft is negative, then i cannot reach j,
        and neither can any station between i and j.
    2. If total gas is larger than the total cost, then there must exist a solution
    Therefore, use gasLeft part to locate the starting position
    use gasSum to check if the solution

    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start=0
        gasLeft=0
        gasSum=0
        for i in range(len(cost)):

            gasDelta=gas[i]-cost[i]
            gasLeft+=gasDelta
            gasSum+=gasDelta
            if gasLeft<0:
                start=i+1
                gasLeft=0

        if gasSum<0:
            return -1
        else:
            return start

