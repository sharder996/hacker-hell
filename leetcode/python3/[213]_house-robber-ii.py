#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
  '''
  Accepted
  74/74 cases passed (24 ms)
  Your runtime beats 95.72 % of python3 submissions
  Your memory usage beats 79.28 % of python3 submissions (14.1 MB)

  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def rob(self, nums: List[int]) -> int:
    def robHelper(lo: int, hi: int) -> int:
      rob, notRob = 0, 0
      for i in range(lo, hi):
        temp = notRob
        notRob = max(notRob, rob)
        rob = temp + nums[i]
      return max(rob, notRob)
    
    if len(nums) == 0:
      return 0
    if len(nums) == 1:
      return nums[0]
    
    return max(robHelper(0, len(nums) - 1), robHelper(1, len(nums)))


  '''
  Accepted
  74/74 cases passed (32 ms)
  Your runtime beats 61.19 % of python3 submissions
  Your memory usage beats 55.45 % of python3 submissions (14.3 MB)

  Time complexity : O(n)
  Space complexity : O(n)
  '''
  def rob(self, nums: List[int]) -> int:
    def robHelper(lo: int, hi: int) -> int:
      if lo == hi - 1:
        return nums[lo]
      
      dp = [0] * len(nums)
      dp[lo] = nums[lo]
      dp[lo+1] = max(dp[lo], nums[lo+1])

      for i in range(lo + 2, hi):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
      return dp[hi-1]

    if len(nums) == 0:
      return 0
    if len(nums) == 1:
      return nums[0]
    
    return max(robHelper(0, len(nums) - 1), robHelper(1, len(nums)))
# @lc code=end

