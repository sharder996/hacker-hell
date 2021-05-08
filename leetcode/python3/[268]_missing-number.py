#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
  '''
  Accepted
  122/122 cases passed (132 ms)
  Your runtime beats 57.99 % of python3 submissions
  Your memory usage beats 95.63 % of python3 submissions (15.3 MB)
  
  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def missingNumber(self, nums: List[int]) -> int:
    ret = int(len(nums) * (len(nums) + 1) / 2)
    for num in nums:
      ret -= num
    
    return ret
# @lc code=end

