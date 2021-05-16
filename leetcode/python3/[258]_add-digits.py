#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
  '''
  Accepted
  1101/1101 cases passed (40 ms)
  Your runtime beats 34.98 % of python3 submissions
  Your memory usage beats 43.6 % of python3 submissions (14.2 MB)

  Time complexity : O(log n)
  Space complexity : O(1)
  '''
  def addDigits(self, num: int) -> int:
    retval = 0

    while num > 0:
      retval += num % 10
      num //= 10

      if num == 0 and retval > 9:
        num = retval
        retval = 0
    
    return retval
  

  '''
  Accepted
  1101/1101 cases passed (24 ms)
  Your runtime beats 96.59 % of python3 submissions
  Your memory usage beats 43.6 % of python3 submissions (14.2 MB)

  Time complexity : O(1)
  Space complexity : O(1)
  '''
  def addDigits(self, num: int) -> int:
    if num == 0:
      return 0
    elif num % 9 == 0:
      return 9
    else:
      return num % 9
# @lc code=end

