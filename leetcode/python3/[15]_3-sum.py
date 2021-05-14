#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
  '''
  Accepted
  318/318 cases passed (848 ms)
  Your runtime beats 74.88 % of python3 submissions
  Your memory usage beats 50.32 % of python3 submissions (17.6 MB)

  Time complexity : O(n^2)
  Space complexity : O(n^2)
  '''
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
      return []

    nums.sort()
    if nums[0] > 0 or nums[-1] < 0:
      return []
    
    retval = []
    for i in range(len(nums) - 2):
      if i != 0 and nums[i] == nums[i - 1]:
        continue
      
      diff = 0 - nums[i]
      l = i + 1
      r = len(nums) - 1
      while l < r:
        if nums[l] + nums[r] < diff:
          l += 1
        elif nums[l] + nums[r] > diff:
          r -= 1
        else:
          retval.append([nums[i], nums[l], nums[r]])
          while l < r and nums[r] == nums[r - 1]:
            r -= 1
          
          l += 1
          r -= 1

    return retval
# @lc code=end

