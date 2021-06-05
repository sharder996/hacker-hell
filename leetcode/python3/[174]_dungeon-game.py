#
# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#

# @lc code=start
class Solution:
  '''
  Accepted
  45/45 cases passed (68 ms)
  Your runtime beats 90.53 % of python3 submissions
  Your memory usage beats 88.59 % of python3 submissions (15 MB)

  Time complexity : O(m * n)
  Space complexity : O(m * n)
  '''
  def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
    dp = [[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]
    dp[-1][-1] = max(1 - dungeon[-1][-1], 1)

    for i in range(len(dungeon) - 2, -1, -1):
      dp[i][-1] = max(dp[i+1][-1] - dungeon[i][-1], 1)
    
    for i in range(len(dungeon[0]) - 2, -1, -1):
      dp[-1][i] = max(dp[-1][i+1] - dungeon[-1][i], 1)
    
    for i in range(len(dungeon) - 2, -1, -1):
      for j in range(len(dungeon[0]) - 2, -1, -1):
        right = max(dp[i][j+1] - dungeon[i][j], 1)
        down = max(dp[i+1][j] - dungeon[i][j], 1)
        dp[i][j] = min(right, down)
    
    return dp[0][0]
# @lc code=end

