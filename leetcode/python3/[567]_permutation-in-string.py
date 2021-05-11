#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
  '''
  Accepted
  106/106 cases passed (80 ms)
  Your runtime beats 50.64 % of python3 submissions
  Your memory usage beats 85.9 % of python3 submissions (14.2 MB)

  Time complexity : O(m + n)
  Space complexity : O(1)
  '''
  def checkInclusion(self, s1: str, s2: str) -> bool:
    if len(s2) < len(s1):
      return False
    
    freqs = [0] * 26
    letters = set()
    for c in s1:
      freqs[ord(c) - ord('a')] += 1
      letters.add(c)
    
    currLength = 0
    for i in range(len(s2)):
      if freqs[ord(s2[i]) - ord('a')] > 0:
        freqs[ord(s2[i]) - ord('a')] -= 1
        currLength += 1
        
        if currLength == len(s1):
          return True
      else:
        if s2[i] in letters:
          while freqs[ord(s2[i]) - ord('a')] <= 0:
            freqs[ord(s2[i - currLength]) - ord('a')] += 1
            currLength -= 1
          freqs[ord(s2[i]) - ord('a')] -= 1
          currLength += 1
        else:
          while currLength > 0:
            freqs[ord(s2[i - currLength]) - ord('a')] += 1
            currLength -= 1
      
      if len(s2) - i + currLength - 1 < len(s1):
        return False
    
    return False
# @lc code=end

