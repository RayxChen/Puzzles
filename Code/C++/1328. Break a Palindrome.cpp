#include<string>
using namespace std;

class Solution {
public:
    string breakPalindrome(string palindrome) {
        // aaa -> aab
        int n = palindrome.size();
        for (int i = 0; i < n / 2; ++i) {
            if (palindrome[i] != 'a') {
                palindrome[i] = 'a';
                return palindrome;
            }
        }
        palindrome[n-1] = 'b';
        return n > 1 ? palindrome : "";
    }
};