#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
  '''
  Accepted
  21/21 cases passed (36 ms)
  Your runtime beats 56.32 % of python3 submissions
  Your memory usage beats 28.08 % of python3 submissions (14.4 MB)

  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    for i in range(len(matrix) // 2):
      for j in range((len(matrix[0]) + (-len(matrix[0]) % 2)) // 2):
        temp = matrix[i][j]
        matrix[i][j] = matrix[len(matrix) - j - 1][i]
        matrix[len(matrix) - j - 1][i] = matrix[len(matrix) - i - 1][len(matrix) - j - 1]
        matrix[len(matrix) - i - 1][len(matrix) - j - 1] = matrix[j][len(matrix) - i - 1]
        matrix[j][len(matrix) - i - 1] = temp
# @lc code=end

