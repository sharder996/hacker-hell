#
# @lc app=leetcode id=419 lang=python3
#
# [419] Battleships in a Board
#

# @lc code=start
class Solution:
  '''
  Accepted
  27/27 cases passed (68 ms)
  Your runtime beats 85.82 % of python3 submissions
  Your memory usage beats 54.1 % of python3 submissions (14.8 MB)

  Time complexity : O(m * n)
  Space complexity : O(1)
  '''
  def countBattleships(self, board: List[List[str]]) -> int:
    retval = 0

    for i in range(len(board)):
      for j in range(len(board[0])):
        if board[i][j] == '.':
          continue
        if i+1 < len(board) and board[i+1][j] == 'X':
          continue
        if j+1 < len(board[0]) and board[i][j+1] == 'X':
          continue
        retval += 1
    
    return retval
# @lc code=end

