#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
  '''
  Accepted
  22/22 cases passed (32 ms)
  Your runtime beats 53.76 % of python3 submissions
  Your memory usage beats 94.59 % of python3 submissions (14 MB)

  Time complexity : O(m * n)
  Space complexity : O(m * n)
  '''
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    retval = []

    l, r, u, d = 0, len(matrix[0]), 0, len(matrix)
    while l < r and u < d:
      for i in range(l, r):
        retval.append(matrix[u][i])
      u += 1
      for i in range(u, d):
        retval.append(matrix[i][r - 1])
      r -= 1
      if u < d:
        for i in range(r - 1, l - 1, -1):
          retval.append(matrix[d - 1][i])
        d -= 1
      if l < r:
        for i in range(d - 1, u - 1, -1):
          retval.append(matrix[i][l])
        l += 1
  
    return retval
# @lc code=end

