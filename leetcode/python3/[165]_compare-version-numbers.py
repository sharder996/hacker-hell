#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
  '''
  Accepted
  81/81 cases passed (28 ms)
  Your runtime beats 81.86 % of python3 submissions
  Your memory usage beats 29.52 % of python3 submissions (14.4 MB)

  Time complexity : O(m + n)
  Space complexity : O(m + n)
  '''
  def compareVersion(self, version1: str, version2: str) -> int:
    version1 = [int(x) for x in version1.split('.')]
    version2 = [int(x) for x in version2.split('.')]

    while 1:
      v1 = version1.pop(0) if version1 else 0
      v2 = version2.pop(0) if version2 else 0

      if v1 < v2:
        return -1
      elif v2 < v1:
        return 1
      elif not version1 and not version2:
        return 0
# @lc code=end

