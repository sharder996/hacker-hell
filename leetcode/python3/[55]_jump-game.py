#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
  '''
  Accepted
  165/165 cases passed (528 ms)
  Your runtime beats 8.26 % of python3 submissions
  Your memory usage beats 90.28 % of python3 submissions (15.2 MB)

  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def canJump(self, nums: List[int]) -> bool:
    i, maxLength = 0, 0
    for i in range(len(nums)):
      if i > maxLength:
        return False
      maxLength = max(i + nums[i], maxLength)
    return True
# @lc code=end

