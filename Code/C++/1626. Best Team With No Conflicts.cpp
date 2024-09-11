#include<vector>
#include<algorithm>

using namespace std;


class Solution {
public:
    int bestTeamScore(vector<int>& scores, vector<int>& ages) {
        int max_age = *max_element(ages.begin(), ages.end());
        vector<int> dp(max_age+1, 0);
        vector<pair<int, int>> pairs;
        for (int i = 0; i < scores.size(); i++) {
            pairs.push_back({scores[i], ages[i]});
        }
        sort(pairs.begin(), pairs.end());
        for (auto &[score, age]: pairs){
            dp[age] = *max_element(dp.begin(), dp.begin() + age + 1) + score; 
        }
        return *max_element(dp.begin(), dp.end());
    }
};