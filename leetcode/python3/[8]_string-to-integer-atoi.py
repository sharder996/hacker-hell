#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
  '''
  Accepted
  1082/1082 cases passed (36 ms)
  Your runtime beats 53.77 % of python3 submissions
  Your memory usage beats 24.16 % of python3 submissions (14.3 MB)
  
  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def myAtoi(self, s: str) -> int:
    if len(s) == 0:
      return 0
    
    i = 0
    while i < len(s) and s[i] == ' ':
      i += 1
    
    if i >= len(s) or s[i] != '-' and s[i] != '+' and (s[i] < '0' or s[i] > '9'):
      return 0
    
    negative = True
    if s[i] != '-':
      negative = False
    if s[i] == '-' or s[i] == '+':
      i += 1
    
    retval = 0
    while i < len(s) and '0' <= s[i] <= '9':
      retval *= 10
      retval += ord(s[i]) - ord('0')

      if negative and retval > pow(2, 31):
        retval = pow(2, 31)
        break
      if not negative and retval > pow(2, 31) - 1:
        retval = pow(2, 31) - 1
        break

      i += 1

    return retval if not negative else retval * -1
# @lc code=end

