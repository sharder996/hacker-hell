#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
  '''
  Accepted
  63/63 cases passed (44 ms)
  Your runtime beats 73.32 % of python3 submissions
  Your memory usage beats 70.83 % of python3 submissions (14.3 MB)

  Time complexity : O(log n)
  Space complexity : O(1)
  '''
  def findPeakElement(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return 0
    
    lo, mid, hi = 0, len(nums) // 2, len(nums) - 1

    while lo <= hi:
      if ((mid == 0 or nums[mid - 1] <= nums[mid]) and \
          (mid == len(nums) - 1 or nums[mid + 1] <= nums[mid])):
        return mid
      elif mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
        hi = mid - 1
        mid = (hi + lo) // 2
      else:
        lo = mid + 1
        mid = (hi + lo) // 2
# @lc code=end

