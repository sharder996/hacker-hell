#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
  '''
  Accepted
  59/59 cases passed (40 ms)
  Your runtime beats 31.03 % of python3 submissions
  Your memory usage beats 85 % of python3 submissions (14.2 MB)

  Time complexity : O(m + n)
  Space complexity : O(1)
  '''
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1Pos, nums2Pos = m - 1, n - 1
    for i in range(m + n - 1, -1, -1):
      if nums2Pos < 0:
        break
      elif nums2Pos >= 0 and nums1Pos >= 0 and nums2[nums2Pos] > nums1[nums1Pos] or nums1Pos < 0:
        nums1[i] = nums2[nums2Pos]
        nums2Pos -= 1
      else:
        nums1[i] = nums1[nums1Pos]
        nums1Pos -= 1
# @lc code=end

