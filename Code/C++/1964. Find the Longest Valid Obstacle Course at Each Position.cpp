#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> longestObstacleCourseAtEachPosition(vector<int>& obstacles) {
        const int n = obstacles.size();
        vector<int> res(n);
        vector<int> cur;
        for (int i=0; i<n; i++){
            int idx = upper_bound(cur.begin(), cur.end(), obstacles[i]) - cur.begin();
            if (idx == cur.size()){
                cur.push_back(obstacles[i]);
            }
            else{
                cur[idx] = obstacles[i];
            }
            res[i] = idx + 1;

        }
        return res;
    }

};
