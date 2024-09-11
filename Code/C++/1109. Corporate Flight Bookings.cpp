#include<vector>

using namespace std;

class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
        vector<int> res(n+1);
        for (auto& booking:bookings){
            int first = booking[0]-1, second = booking[1], k = booking[2];
            res[first] += k;
            res[second] -= k;
        }
        for (int i=1;i<=n;i++){
            res[i] += res[i-1];
        }
        res.pop_back();
        return res;

    }
};