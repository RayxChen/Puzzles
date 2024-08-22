#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        //  (n+1) element -> i <= n
        vector<pair<int, int>> intervals;
        pair<int, int> tmp;
        for (int i = 0; i <= n; i++) {
            int left_span = max(0, i - ranges[i]);
            int right_span = min(n, i + ranges[i]);
            intervals.push_back({left_span, right_span});
        }
        sort(intervals.begin(), intervals.end());

        int end = 0, farthest = 0, res = 0, i = 0;
        while (end < n){
            while (i <= n && intervals[i].first <= end){
                farthest = max(farthest, intervals[i].second);
                i++;
            }
            if (farthest == end) {return -1;}
            res ++;
            end = farthest;
        }
        return res;

    }
};