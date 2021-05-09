#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
  '''
  Accepted
  18/18 cases passed (24 ms)
  Your runtime beats 92.32 % of python3 submissions
  Your memory usage beats 70.27 % of python3 submissions (14.2 MB)
  
  Time complexity : O(log n)
  Space complexity : O(log n)
  '''
  def convertToTitle(self, columnNumber: int) -> str:
    retval = ''
    while columnNumber > 0:
      retval = chr(ord('A') + ((columnNumber % 26) - 1) % 26) + retval
      columnNumber = int((columnNumber - 1) / 26)
    
    return retval
# @lc code=end

