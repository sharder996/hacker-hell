#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
  '''
  Accepted
  195/195 cases passed (32 ms)
  Your runtime beats 97.31 % of python3 submissions
  Your memory usage beats 52.83 % of python3 submissions (14.6 MB)

  Time complexity : O(log n)
  Space complexity : O(1)
  '''
  def search(self, nums: List[int], target: int) -> int:
    lo, mid, hi = 0, len(nums) // 2, len(nums) - 1

    while lo <= hi:
      if nums[mid] == target:
        return mid
      elif target < nums[mid] and target <= nums[hi] < nums[mid] or \
          target > nums[mid] > nums[hi] or \
          nums[mid] < target <= nums[hi]:
        lo = mid + 1
        mid = (lo + hi) // 2
      else:
        hi = mid - 1
        mid = (lo + hi) // 2
    
    return -1
# @lc code=end

