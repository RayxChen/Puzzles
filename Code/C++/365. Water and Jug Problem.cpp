#include <numeric> 

using namespace std;

class Solution {
public:
    bool canMeasureWater(int x, int y, int target) {
        if (target > (x+y) || target % gcd(x, y) != 0 ){
            return false;
        }
        return true;
    }
};