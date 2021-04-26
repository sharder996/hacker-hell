/*
 * @lc app=leetcode id=5 lang=cpp
 *
 * [5] Longest Palindromic Substring
 */

// @lc code=start
class Solution {
public:
  /*
  * Accepted
  * 176/176 cases passed (88 ms)
  * Your runtime beats 56.56 % of cpp submissions
  * Your memory usage beats 22.48 % of cpp submissions (231.5 MB)
  * 
  * Time complexity : O(n^2)
  * Space complexity : O(1)
  */
  string longestPalindrome(string s) {
    int left = 0, right = 0;
    for (int i = 0; i < s.size(); i++) {
      int length = max(expand(s, i, i), expand(s, i, i + 1));

      if (length > right - left) {
        left = i - (length - 1) / 2;
        right = i + length / 2;
      }
    }

    return s.substr(left, right - left + 1);
  }

  int expand(string s, int left, int right) {
    while (left >= 0 && right < s.size() && s[left] == s[right]) {
      left--;
      right++;
    }

    return right - left - 1;
  }
};
// @lc code=end

