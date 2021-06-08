#
# @lc app=leetcode id=722 lang=python3
#
# [722] Remove Comments
#

# @lc code=start
class Solution:
  '''
  Accepted
  53/53 cases passed (28 ms)
  Your runtime beats 84.46 % of python3 submissions
  Your memory usage beats 74.91 % of python3 submissions (14.2 MB)

  Time complexity : O(m * n) where m is the average length of a line
  Space complexity : O(m * n) where m is the average length of a line
  '''
  # def removeComments(self, source: List[str]) -> List[str]:
  def removeComments(self, source):
    retval = []
    mode = False
    temp = ''
    for line in source:
      i = 0
      while i < len(line):
        if mode:
          if line[i] == '*' and i < len(line) - 1 and line[i+1] == '/':
            mode = False
            i += 1
        else:
          if line[i] == '/' and i < len(line) - 1 and line[i+1] == '/':
            break
          elif line[i] == '/' and i < len(line) - 1 and line[i+1] == '*':
            mode = True
            i += 1
          else:
            temp += line[i]
        i += 1
      if not mode and temp:
        retval.append(temp)
        temp = ''

    return retval
# @lc code=end

