#include <vector>
#include <numeric>
#include <algorithm>
#include <cstring>

using namespace std;

#include <vector>
#include <numeric>
#include <algorithm>
#include <cstring>

using namespace std;

class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        int n = piles.size();
        vector<int> suffix(n+1);
        vector<vector<int>> dp(n+1, vector<int>(n+1, -1));
        for (int i = n-1; i>=0; i--){
            suffix[i] = suffix[i+1] + piles[i];
        }
        return dfs(0, 1, suffix, dp);

    }

    int dfs(int i, int m, vector<int> &suffix, vector<vector<int>> &dp){
        if (i >= suffix.size() - 1) {return 0;}
        if (dp[i][m] != -1) {return dp[i][m];}
        int res = 0;
        for (int x=1; x<=2*m; x++){
            if (i + x <= suffix.size() - 1){
                res = max(res, suffix[i] - dfs(i+x, max(x, m), suffix, dp));
            }
        }
        dp[i][m] = res;
        return res;
    }

};