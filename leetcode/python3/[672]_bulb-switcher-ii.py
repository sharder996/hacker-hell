#
# @lc app=leetcode id=672 lang=python3
#
# [672] Bulb Switcher II
#

# @lc code=start
class Solution:
  '''
  Accepted
  80/80 cases passed (40 ms)
  Your runtime beats 16.92 % of python3 submissions
  Your memory usage beats 98.46 % of python3 submissions (14 MB)

  Time complexity : O(1)
  Space complexity : O(1)
  '''
  def flipLights(self, n: int, presses: int) -> int:
    if presses == 0:
      return 1
    if n == 1:
      return 2
    if presses == 1 and n == 2:
      return 3
    if presses == 1 or n == 2:
      return 4
    if presses == 2:
      return 7
    return 8
# @lc code=end

