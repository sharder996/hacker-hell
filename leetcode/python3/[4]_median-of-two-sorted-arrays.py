#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
  '''
  Accepted
  2094/2094 cases passed (96 ms)
  Your runtime beats 47.06 % of python3 submissions
  Your memory usage beats 54.94 % of python3 submissions (14.5 MB)

  Time complexity : O((m+n)/2)
  Space complexity : O(1)
  '''
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    nums1Pos, nums2Pos = 0, 0
    prevVal, currVal = 0, 0

    for i in range(int((len(nums1) + len(nums2)) / 2) + 1):
      if nums2Pos == len(nums2) or (nums1Pos < len(nums1) and nums1[nums1Pos] <= nums2[nums2Pos]):
        prevVal = currVal
        currVal = nums1[nums1Pos]
        nums1Pos += 1
      else:
        prevVal = currVal
        currVal = nums2[nums2Pos]
        nums2Pos += 1
    
    return (prevVal + currVal) / 2 if (len(nums1) + len(nums2)) % 2 == 0 else currVal
# @lc code=end

