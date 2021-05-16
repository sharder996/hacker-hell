#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
  '''
  Accepted
  3999/3999 cases passed (44 ms)
  Your runtime beats 78.58 % of python3 submissions
  Your memory usage beats 25.43 % of python3 submissions (14.4 MB)

  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def romanToInt(self, s: str) -> int:
    retval = 0

    i = 0
    while i < len(s):
      if s[i] == 'M':
        retval += 1000
      elif s[i] == 'D':
        retval += 500
      elif s[i] == 'C':
        if i + 1 < len(s) and s[i + 1] == 'D':
          retval += 400
          i += 1
        elif i + 1 < len(s) and s[i + 1] == 'M':
          retval += 900
          i += 1
        else:
          retval += 100
      elif s[i] == 'L':
        retval += 50
      elif s[i] == 'X':
        if i + 1 < len(s) and s[i + 1] == 'L':
          retval += 40
          i += 1
        elif i + 1 < len(s) and s[i + 1] == 'C':
          retval += 90
          i += 1
        else:
          retval += 10
      elif s[i] == 'V':
        retval += 5
      else:
        if i + 1 < len(s) and s[i + 1] == 'V':
          retval += 4
          i += 1
        elif i + 1 < len(s) and s[i + 1] == 'X':
          retval += 9
          i += 1
        else:
          retval += 1
      
      i += 1

    return retval
# @lc code=end

