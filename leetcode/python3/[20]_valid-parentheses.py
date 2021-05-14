#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
  '''
  Accepted
  91/91 cases passed (32 ms)
  Your runtime beats 82.24 % of python3 submissions
  Your memory usage beats 64.27 % of python3 submissions (14.2 MB)

  Time complexity : O(n)
  Space complexity : O(n)
  '''
  def isValid(self, s: str) -> bool:
    if len(s) % 2 == 1:
      return False
    
    stack = list()
    for c in s:
      if c == '[' or c == '(' or c == '{':
        stack.append(c)
      else:
        if len(stack) > 0 and 1 <= ord(c) - ord(stack.pop()) <= 2:
          continue
        return False
    
    if len(stack) > 0:
      return False
    return True
# @lc code=end

