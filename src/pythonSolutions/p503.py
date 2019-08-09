
"""
Next_Greater_Element_II
"""
class Solution:
    """
    @param nums: an array
    @return: the Next Greater Number for every element
    """

    def nextGreaterElements(self, nums):
        # Write your code here
        n = len(nums)
        arr = [None] * n # this can be initialized to -1 to save some time for the largest ones
        stack = []  # stack has [val, index] tuples
        for i in range(n):
            while stack and stack[-1][0] < nums[i]:  # resolving previous items in stack
                _, pos = stack.pop()
                arr[pos] = nums[i]
            stack.append([nums[i], i])  # add current one to the stack

            # now handle the remaining (in stack)

        # the bottom ones ARE the largest
        k = 0
        while k < len(stack) and stack[k][0] == stack[0][0]:
            arr[stack[k][1]] = -1
            k += 1

        # the leftovers: from the last posn circle to the largest num's posn to pop again
        # since it's a circle ...duh... so circle it....(just no need to add anymore
        if k < len(stack):
            start = stack[-1][1] + 1
            end = stack[0][1] + n
            for j in range(start, end + 1):
                j %= n
                while stack[-1][0] < nums[j]:
                    _, pos = stack.pop()
                    arr[pos] = nums[j]
        return arr