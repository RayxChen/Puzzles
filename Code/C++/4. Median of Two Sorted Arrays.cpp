#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& A, vector<int>& B) {
        const int n1 = A.size();
        const int n2 = B.size();
        if (n1 > n2){
            return findMedianSortedArrays(B, A);
        }

        const int k = (n1 + n2 + 1) / 2;
        int l = 0, r = n1;
        
        while (l < r){
            const int m1 = l + (r-l)/2;
            const int m2 = k - m1;
            if (A[m1] < B[m2-1]){
                l = m1 + 1;
            }
            else{
                r = m1;
            }
        }
        const int m1 = l;
        const int m2 = k - m1;
        const int c1 = max(m1>=1 ? A[m1-1] : INT_MIN, m2>=1 ? B[m2-1] : INT_MIN);
        if ((n1 + n2) % 2 == 1){
            return c1;
        }
        const int c2 = min(m1 < n1 ? A[m1] : INT_MAX, m2 < n2 ? B[m2] : INT_MAX);
        return (c1 + c2) * 0.5;
    }
};