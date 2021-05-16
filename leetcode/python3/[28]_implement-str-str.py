#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
  '''
  Accepted
  79/79 cases passed (48 ms)
  Your runtime beats 12.72 % of python3 submissions
  Your memory usage beats 24.7 % of python3 submissions (14.6 MB)

  Time complexity : O(m * n)
  Space complexity : O(1)
  '''
  def strStr(self, haystack: str, needle: str) -> int:
    if len(needle) == 0:
      return 0
    
    for i in range(len(haystack)):
      if i + len(needle) <= len(haystack) and haystack[i:i + len(needle)] == needle:
        return i
    
    return -1
# @lc code=end

