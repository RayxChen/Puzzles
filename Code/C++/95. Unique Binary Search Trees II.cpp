#include <vector>
#include <string>
#include <unordered_map>
#include <functional>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        if (n == 0) return {};

        // Memoization map
        unordered_map<string, vector<TreeNode*>> memo;

        // Helper function to generate all unique BSTs for the range [l, r]
        function<vector<TreeNode*>(int, int)> dfs = [&](int l, int r) -> vector<TreeNode*> {
            string key = to_string(l) + "," + to_string(r);
            if (memo.find(key) != memo.end()) {
                return memo[key];
            }
            
            if (l > r) {
                return {nullptr};
            }

            vector<TreeNode*> res;
            for (int i = l; i <= r; ++i) {
                vector<TreeNode*> leftTrees = dfs(l, i - 1);
                vector<TreeNode*> rightTrees = dfs(i + 1, r);
                for (auto left : leftTrees) {
                    for (auto right : rightTrees) {
                        TreeNode* root = new TreeNode(i, left, right);
                        res.push_back(root);
                    }
                }
            }

            memo[key] = res;
            return res;
        };

        return dfs(1, n);
    }
};
