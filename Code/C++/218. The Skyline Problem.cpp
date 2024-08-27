#include <vector>
#include <queue>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<tuple<int, int, int>> events;

        for (auto& building : buildings) {
            int L = building[0], R = building[1], H = building[2];
            events.push_back({L, -H, R});
            events.push_back({R, 0, 0});
        }

        sort(events.begin(), events.end());

        priority_queue<pair<int, int>> pq;
        pq.push({0, INT_MAX});

        vector<vector<int>> res;
        int prevHeight = 0;

        for (auto& [L, negH, R] : events) {
            if (negH != 0) {
                pq.push({-negH, R});
            } else {
                while (!pq.empty() && pq.top().second <= L) {
                    pq.pop();
                }
            }

            int currHeight = pq.empty() ? 0 : pq.top().first;

            if (currHeight != prevHeight) {
                res.push_back({L, currHeight});
                prevHeight = currHeight;
            }
        }

        return res;
    }
};
