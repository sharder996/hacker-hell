#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
  '''
  Accepted
  57/57 cases passed (24 ms)
  Your runtime beats 96.69 % of python3 submissions
  Your memory usage beats 37.74 % of python3 submissions (14.5 MB)

  Time complexity : O(n)
  Space complexity : O(n)
  '''
  def reverseWords(self, s: str) -> str:
    return ' '.join(s.split()[::-1])
# @lc code=end

