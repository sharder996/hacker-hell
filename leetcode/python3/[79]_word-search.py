#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
  '''
  Accepted
  50/50 cases passed (4792 ms)
  Your runtime beats 34.05 % of python3 submissions
  Your memory usage beats 42.02 % of python3 submissions (14.4 MB)

  Time complexity : O((m * n)^2)
  Space complexity : O(m * n)
  '''
  def exist(self, board: List[List[str]], word: str) -> bool:
    if len(word) > len(board) * len(board[0]):
      return False

    for i in range(len(board)):
      for j in range(len(board[0])):
        if board[i][j] == word[0]:
          if self.dfs(board, word, i, j, 0, [[False for _ in range(len(board[0]))] for _ in range(len(board))]):
            return True
    
  
  def dfs(self, board: List[List[str]], word: str, row: int, col: int, char: int, visited: List[List[bool]]):
    if char == len(word):
      return True
    
    if not (0 <= row < len(board)) or not (0 <= col < len(board[0])) \
        or visited[row][col] or board[row][col] != word[char]:
      return False
    
    visited[row][col] = True

    if self.dfs(board, word, row + 1, col, char + 1, visited) or \
        self.dfs(board, word, row - 1, col, char + 1, visited) or \
        self.dfs(board, word, row, col + 1, char + 1, visited) or \
        self.dfs(board, word, row, col - 1, char + 1, visited):
      return True

    visited[row][col] = False
    return False
# @lc code=end

