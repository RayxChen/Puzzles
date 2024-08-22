#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
    long long minCost(vector<int>& nums, vector<int>& cost) {
        int l = *min_element(nums.begin(), nums.end());
        int r = *max_element(nums.begin(), nums.end());
        while (l < r){
            const int mid = l + (r-l) / 2;
            if (f(nums, cost, mid) > f(nums, cost, mid + 1)){
                l = mid + 1;
            }
            else{
                r = mid;
            }
        }
        return f(nums, cost, l);
    }

    long long f(vector<int>& nums, vector<int>& cost, const int x){
        const int n = nums.size();
        long long totalCost = 0;

        for (int i=0;i<n;i++){
            totalCost += 1LL* abs(nums[i] - x) * cost[i];
        }
        return totalCost;
    }
};