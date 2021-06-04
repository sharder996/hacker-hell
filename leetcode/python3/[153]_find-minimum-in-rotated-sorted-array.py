#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
  '''
  Accepted
  150/150 cases passed (40 ms)
  Your runtime beats 65.91 % of python3 submissions
  Your memory usage beats 82.64 % of python3 submissions (14.4 MB)

  Time complexity : O(log n)
  Space complexity : O(1)
  '''
  def findMin(self, nums) -> int:
    lo, mid, hi = 0, len(nums) // 2, len(nums) - 1

    if nums[lo] < nums[hi]:
      return nums[0]

    while lo < hi - 1:
      if nums[mid] >= nums[lo] >= nums[hi]:
        lo = mid
        mid = (lo + hi) // 2
      else:
        hi = mid
        mid = (lo + hi) // 2
    
    return nums[hi]
# @lc code=end
