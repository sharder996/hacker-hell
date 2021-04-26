/*
 * @lc app=leetcode id=4 lang=cpp
 *
 * [4] Median of Two Sorted Arrays
 */

// @lc code=start
class Solution {
public:
  /*
  * Accepted
  * 2094/2094 cases passed (20 ms)
  * Your runtime beats 93.61 % of cpp submissions
  * Your memory usage beats 73.07 % of cpp submissions (89 MB)
  * 
  * Time complexity : O((m+n)/2)
  * Space complexity : O(1)
  */
  double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    int num1Pos = 0, num2Pos = 0;
    int prevVal = 0, currVal = 0;

    for (int i = 0; i < ((nums1.size() + nums2.size()) / 2) + 1; i++) {
      if (num2Pos == nums2.size() || (num1Pos < nums1.size() && nums1[num1Pos] < nums2[num2Pos])) {
        prevVal = currVal;
        currVal = nums1[num1Pos++];
      } else {
        prevVal = currVal;
        currVal = nums2[num2Pos++];
      }
    }

    return (nums1.size() + nums2.size()) % 2 == 0 ?(double)(prevVal + currVal) / 2 : currVal;
  }
};
// @lc code=end

