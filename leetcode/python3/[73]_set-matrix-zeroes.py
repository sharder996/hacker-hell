#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
  '''
  Accepted
  164/164 cases passed (128 ms)
  Your runtime beats 72.26 % of python3 submissions
  Your memory usage beats 99.68 % of python3 submissions (14.7 MB)

  Time complexity : O(m * n)
  Space complexity : O(1)
  '''
  def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    firstRow = False
    firstCol = False

    for i in range(len(matrix)):
      if matrix[i][0] == 0:
        firstCol = True
        break
    
    for j in range(len(matrix[0])):
      if matrix[0][j] == 0:
        firstRow = True
        break

    for i in range(1, len(matrix)):
      for j in range(1, len(matrix[0])):
        if matrix[i][j] == 0:
          matrix[i][0] = 0
          matrix[0][j] = 0
    
    for i in range(1, len(matrix)):
      if matrix[i][0] == 0:
        for j in range(1, len(matrix[0])):
          matrix[i][j] = 0
    
    for j in range(1, len(matrix[0])):
      if matrix[0][j] == 0:
        for i in range(1, len(matrix)):
          matrix[i][j] = 0
    
    if firstCol:
      for i in range(len(matrix)):
        matrix[i][0] = 0
    if firstRow:
      for j in range(len(matrix[0])):
        matrix[0][j] = 0
# @lc code=end

