/*
 * @lc app=leetcode id=2 lang=cpp
 *
 * [2] Add Two Numbers
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
  /*
  Accepted
  1568/1568 cases passed (20 ms)
  Your runtime beats 92.15 % of cpp submissions
  Your memory usage beats 13.05 % of cpp submissions (71.2 MB)

  Time complexity : O(max(m,n))
  Space complexity : O(max(m,n))
  */
  ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode *l3 = NULL;
    ListNode **next = &l3;

    int sum = 0;
    while (l1 != NULL || l2 != NULL || sum > 0) {
      if (l1 != NULL) {
        sum += l1->val;
        l1 = l1->next;
      }

      if (l2 != NULL) {
        sum += l2->val;
        l2 = l2->next;
      }

      (*next) = new ListNode(sum % 10);
      sum /= 10;
      next = &((*next)->next);
    }

    return l3;
  }
};
// @lc code=end

