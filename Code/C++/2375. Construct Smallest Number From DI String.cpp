#include<string>
#include<stack>
#include <algorithm>

using namespace std;

class Solution {
public:
    string smallestNumber(string pattern) {
        int n = pattern.size();
        stack<int> stack;
        string res = "";
        for (int i=0; i<=n;i++){
            stack.push(i+1);
            if (i == n || pattern[i] == 'I'){
                while (!stack.empty()){
                    res += to_string(stack.top());
                    stack.pop();
                }
            }
            
        }
        return res;
    }
};