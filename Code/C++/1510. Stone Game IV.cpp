#include <vector>

using namespace std;

class Solution {
public:
    bool winnerSquareGame(int n) {
        vector<int> dp(n+1, false);
        for (int i=1; i < dp.size(); i++){
            for (int j=1; j*j<=i;j++){
                if (!dp[i-j*j]){
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }
};
