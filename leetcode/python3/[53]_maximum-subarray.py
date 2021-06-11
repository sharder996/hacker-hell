#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
  '''
  Accepted
  203/203 cases passed (68 ms)
  Your runtime beats 50.59 % of python3 submissions
  Your memory usage beats 13.47 % of python3 submissions (15.1 MB)

  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def maxSubArray(self, nums: List[int]) -> int:
    maxi = nums[0]
    total = nums[0]
    for i in range(1, len(nums)):
      total = max(nums[i], total + nums[i])
      maxi = max(maxi, total)
    
    return maxi
# @lc code=end

