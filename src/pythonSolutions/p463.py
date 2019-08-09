class Solution:
    """
    @param grid: a 2D array
    @return: the perimeter of the island
    """
    total = 0

    def islandPerimeter(self, grid):
        # Write your code here
        self.total = 0
        startNodeRow, startNodeCol = self.findFirstNode(grid)

        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        queue = []  # records where to look next
        visited[startNodeRow][startNodeCol] = 1
        queue.append([startNodeRow, startNodeCol, (0, 1)])  # look to the right
        queue.append([startNodeRow, startNodeCol, (1, 0)])  # look down
        # no need to look left or up since we came from upper-left direction
        self.total += 2  # and thus left and up sides are counted

        while queue:
            node_row, node_col, direction = queue.pop(0)
            visited[node_row][node_col] = 1

            next_row, next_col = node_row + direction[0], node_col + direction[1]
            if next_row >= m or next_col >= n or next_row<0 or next_col<0:

                self.total += 1
            elif visited[next_row][next_col]:
                continue
            elif grid[next_row][next_col] == 1:
                visited[next_row][next_col]=1
                for d in [(0,1),(0,-1),(1,0),(-1,0)]:
                    queue.append([next_row, next_col, d])
                    # there's one unnecessary direction, i'll let the visited grid handle that
            else:
                self.total += 1

        return self.total

    def findFirstNode(self,grid):
        for i in range(len(grid)):  # move to next row (going down)
            for j in range(len(grid[0])):  # searching in the 'right' direction
                if grid[i][j] == 1:
                    return i, j   # found the starting point and return



test_data=[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
test_data1=[[1,1]]
test_data2=[[1,1],[1,1]]
# print(Solution().islandPerimeter(test_data))
print(Solution().islandPerimeter(test_data2))
