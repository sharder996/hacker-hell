#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
  '''
  Accepted
  480/480 cases passed (56 ms)
  Your runtime beats 22.46 % of python3 submissions
  Your memory usage beats 92.93 % of python3 submissions (14.5 MB)

  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def isPalindrome(self, s: str) -> bool:
    lo, hi = 0, len(s) - 1
    # s = s.lower()

    while lo < hi:
      while lo < hi and not ('a' <= s[lo].lower() <= 'z') and not ('0' <= s[lo].lower() <= '9'):
        lo += 1
      while lo < hi and not ('a' <= s[hi].lower() <= 'z') and not ('0' <= s[hi].lower() <= '9'):
        hi -= 1
      
      if s[lo].lower() != s[hi].lower():
        return False
      
      lo += 1
      hi -= 1
    
    return True
# @lc code=end

