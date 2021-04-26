/*
 * @lc app=leetcode id=3 lang=cpp
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
class Solution {
public:
  /*
  * Time Limit Exceeded
  * 986/987 cases passed (N/A)
  * 
  * Time complexity : O(n^3)
  * Space complexity : O(min(m,n)) where m is the size of the charset
  */
  int lengthOfLongestSubstring(string s) {
    int longest = 0;

    for (int i = 0; i < s.size(); i++) {
      for (int j = i; j < s.size(); j++) {
        set<char> set;
        bool dup = false;
        for (int k = i; k < j + 1; k++) {
          if (set.find(s[k]) != set.end()) {
            longest = max(k - i, longest);
            dup = true;
            break;
          }

          set.insert(s[k]);
        }

        if (!dup) {
          longest = max(j - i + 1, longest);
        }
      }
    }

    return longest;
  }


  /*
  * Accepted
  * 987/987 cases passed (8 ms)
  * Your runtime beats 85.77 % of cpp submissions
  * Your memory usage beats 44.04 % of cpp submissions (8.4 MB)
  * 
  * Time complexity : O(n)
  * Space complexity : O(min(m,n)) where m is the size of the charset
  */
  int lengthOfLongestSubstring(string s) {
    map<char, int> map;
    std::map<char, int>::iterator it;
    int start = 0;
    int len = 0;

    for (int i = 0; i < s.size(); i++) {
      it = map.find(s[i]);
      if (it != map.end()) {
        start = max(it->second + 1, start);
      }

      map[s[i]] = i;
      len = max(i - start + 1, len);
    }

    return len;
  }
};
// @lc code=end

