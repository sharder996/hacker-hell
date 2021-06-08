#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#

# @lc code=start
class Solution:
  '''
  Accepted
  28/28 cases passed (28 ms)
  Your runtime beats 88 % of python3 submissions
  Your memory usage beats 68.84 % of python3 submissions (14.2 MB)

  Time complexity : O(log(jug1Capacity * jug2Capacity))
  Space complexity : O(1)
  '''
  def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
    return targetCapacity == 0 or (jug1Capacity + jug2Capacity >= targetCapacity and 
      targetCapacity % self.gcd(jug1Capacity, jug2Capacity) == 0)
  
  def gcd(self, x, y):
    return x if y == 0 else self.gcd(y, x % y)
# @lc code=end

