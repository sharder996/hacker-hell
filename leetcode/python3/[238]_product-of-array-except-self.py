#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
  '''
  Accepted
  20/20 cases passed (224 ms)
  Your runtime beats 93.7 % of python3 submissions
  Your memory usage beats 81.83 % of python3 submissions (21.1 MB)

  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    retval = [0] * len(nums)
    temp = 1

    for i in range(len(retval)):
      retval[i] = temp
      temp *= nums[i]

    temp = 1
    for i in range(len(retval) - 1, -1, -1):
      retval[i] *= temp
      temp *= nums[i]

    return retval
# @lc code=end

