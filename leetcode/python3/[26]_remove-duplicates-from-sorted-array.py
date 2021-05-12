#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
  '''
  Accepted
  161/161 cases passed (80 ms)
  Your runtime beats 79.51 % of python3 submissions
  Your memory usage beats 51.43 % of python3 submissions (15.9 MB)

  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def removeDuplicates(self, nums: List[int]) -> int:
    if len(nums) == 0:
      return 0
    position = 0

    for i in range(1, len(nums)):
      if nums[position] != nums[i]:
        position += 1
        nums[position] = nums[i]
    
    return position + 1
# @lc code=end

