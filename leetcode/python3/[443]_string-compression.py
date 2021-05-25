#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
  '''
  Accepted
  70/70 cases passed (48 ms)
  Your runtime beats 97.42 % of python3 submissions
  Your memory usage beats 5.4 % of python3 submissions (14.6 MB)

  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def compress(self, chars: List[str]) -> int:
    retval = 0

    comPos = 1
    pos = 1
    length = 1
    while pos < len(chars) + 1:
      if pos < len(chars) and chars[pos] == chars[pos - 1]:
        length += 1
        pos += 1
      else:
        if length > 1:
          for char in str(length):
            chars[comPos] = char
            comPos += 1
        if pos < len(chars):
          chars[comPos] = chars[pos]

        length = 1
        comPos += 1
        pos += 1
    
    return comPos - 1
# @lc code=end

