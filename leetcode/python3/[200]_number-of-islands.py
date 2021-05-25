#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
  '''
  Accepted
  48/48 cases passed (132 ms)
  Your runtime beats 85.74 % of python3 submissions
  Your memory usage beats 35.5 % of python3 submissions (15.6 MB)

  Time complexity : O(m * n)
  Space complexity : O(1)
  '''
  def numIslands(self, grid: List[List[str]]) -> int:
    def dfs(row: int, col: int):
      if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == '1':
        grid[row][col] = '0'
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)
    
    retval = 0

    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == '1':
          retval += 1
          dfs(i, j)
    
    return retval
# @lc code=end

