#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        const int n = stations.size();
        priority_queue<int> pq;
        int res=0;
        int i=0;
        while (startFuel < target){
            while (i < n && stations[i][0] <= startFuel){
                pq.push(stations[i][1]);
                i++;
            }
            if (pq.empty()){
                return -1;
            }
            startFuel += pq.top();
            pq.pop();
            res++;
        }
        return res;

    }

};