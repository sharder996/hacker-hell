#
# @lc app=leetcode id=650 lang=python3
#
# [650] 2 Keys Keyboard
#

# @lc code=start
class Solution:
  '''
  Accepted
  126/126 cases passed (24 ms)
  Your runtime beats 98.48 % of python3 submissions
  Your memory usage beats 79.91 % of python3 submissions (14.1 MB)
  
  Time complexity : O(log n)
  Space complexity : O(1)
  '''
  def minSteps(self, n: int) -> int:
    if n == 1:
      return 0
    if n <= 3:
      return n

    ret = 0
    i = 2
    while i <= n:
      if n % i == 0:
        ret += i
        n /= i
        i = 2
      else:
        i += 1
    
    return ret
# @lc code=end
