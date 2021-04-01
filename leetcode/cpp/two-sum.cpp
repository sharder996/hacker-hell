/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
public:
  /*
  Accepted
  53/53 cases passed (8 ms)
  Your runtime beats 62.21 % of cpp submissions
  Your memory usage beats 53.8 % of cpp submissions (8.9 MB)
  
  Time complexity : O(n^2)
  Space complexity : O(1)
  */
  vector<int> twoSum(vector<int>& nums, int target) {
    for (int i = 0; i < nums.size(); i++) {
      for (int j = 0; j < nums.size(); j++) {
        if (i != j) {
          if (nums[i] + nums[j] == target) {
            return { i, j };
          }
        }
      }
    }

    return {};
  }


  // /*
  // Accepted
  // 53/53 cases passed (4 ms)
  // Your runtime beats 94.97 % of cpp submissions
  // Your memory usage beats 95.81 % of cpp submissions (8.7 MB)
  
  // Time complexity : O(n)
  // Space complexity : O(n)
  // */
  // vector<int> twoSum(vector<int>& nums, int target) {
  //   map<int, int> map;
  //   std::map<int, int>::iterator it;

  //   for (int i = 0; i < nums.size(); i++) {
  //     it = map.find(target - nums[i]);
  //     if (it != map.end()) {
  //       return { it->second, i };
  //     }

  //     map.insert(pair<int, int>(nums[i], i));
  //   }

  //   return {};
  // }
};
// @lc code=end

