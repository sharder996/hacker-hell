#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
  '''
  Accepted
  87/87 cases passed (32 ms)
  Your runtime beats 71.8 % of python3 submissions
  Your memory usage beats 10.38 % of python3 submissions (14.3 MB)

  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) < 2:
      return

    lo, mid, hi = 0, 0, len(nums) - 1
    while mid <= hi:
      if nums[mid] == 0:
        nums[lo], nums[mid] = nums[mid], nums[lo]
        lo += 1
        mid += 1
      elif nums[mid] == 1:
        mid += 1
      else:
        nums[hi], nums[mid] = nums[mid], nums[hi]
        hi -= 1
# @lc code=end

