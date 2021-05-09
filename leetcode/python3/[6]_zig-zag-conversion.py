#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
  '''
  Accepted
  1157/1157 cases passed (76 ms)
  Your runtime beats 24.34 % of python3 submissions
  Your memory usage beats 69.68 % of python3 submissions (14.3 MB)

  Time complexity : O(n)
  Space complexity : O(n)
  '''
  def convert(self, s: str, numRows: int) -> str:
    if numRows == 1:
      return s
    
    rows = [[] for _ in range(numRows)]

    ascending = True
    i = 0
    for c in s:
      rows[i].append(c)
      if ascending:
        i += 1
        if i == numRows - 1:
          ascending = False
      else:
        i -= 1
        if i == 0:
          ascending = True
    
    return ''.join([''.join(c) for row in rows for c in row])
# @lc code=end

