#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
  '''
  Accepted
  176/176 cases passed (980 ms)
  Your runtime beats 69.83 % of python3 submissions
  Your memory usage beats 83.03 % of python3 submissions (14.3 MB)

  Time complexity : O(n^2)
  Space complexity : O(1)
  '''
  def longestPalindrome(self, s: str) -> str:
    left = right = 0
    for i in range(len(s)):
      length = max(self.expand(s, i, i), self.expand(s, i, i + 1))

      if length > right - left:
        left = i - (length - 1) // 2
        right = i + length // 2
    
    return s[left:right+1]

  def expand(self, s: str, left: int, right: int) -> int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
      left -= 1
      right += 1
    return right - left - 1
# @lc code=end

