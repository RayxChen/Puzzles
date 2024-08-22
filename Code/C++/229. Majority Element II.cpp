#include <vector>

using namespace std;

class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int a = 0, b = 0, c1 = 0, c2 = 0, d1 = 0, d2 = 0;
        vector<int> res;
        for (int num:nums){
            if (c1 == 0 && num != b){
                a = num;
                c1 = 1;
            }
            else if (c2 == 0 && num != a){
                b = num;
                c2 = 1;
            }
            else if (num == a){c1++;}
            else if (num == b){c2++;}
            else {
                c1--;
                c2--;
            }
        }
        for (int num: nums){
            if (a == num){d1++;}
            else if (b == num){d2++;}
        }
        const int n = nums.size();
        if (d1 > n/3){res.push_back(a);}
        if (d2 > n/3){res.push_back(b);}
        return res;
    }
};