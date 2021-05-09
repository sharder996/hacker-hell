#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
  '''
  Accepted
  1002/1002 cases passed (32 ms)
  Your runtime beats 67.77 % of python3 submissions
  Your memory usage beats 42.94 % of python3 submissions (14.2 MB)
  
  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def titleToNumber(self, columnTitle: str) -> int:
    retval = 0
    for i in range(len(columnTitle) - 1, -1, -1):
      retval += (ord(columnTitle[i]) - ord('A') + 1) * pow(26, (len(columnTitle) - i - 1))
    
    return retval
# @lc code=end

