#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
class Solution:
  '''
  Accepted
  44/44 cases passed (392 ms)
  Your runtime beats 94.39 % of python3 submissions
  Your memory usage beats 44.47 % of python3 submissions (19.5 MB)

  Time complexity : O(n log n)
  Space complexity : O(1)
  '''
  def findMinArrowShots(self, points: List[List[int]]) -> int:
    points.sort(key=lambda x: x[1])

    retval = 1
    curr = points[0]
    for i in range(1, len(points)):
      if points[i][0] > curr[1]:
        retval += 1
        curr = points[i]
    
    return retval
# @lc code=end

