#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        unordered_map<int, vector<pair<int, double>>> graph;
        for (int i=0; i<edges.size(); i++){
            int a = edges[i][0];
            int b = edges[i][1];
            double prob = succProb[i];
            graph[a].push_back({b, prob});
            graph[b].push_back({a, prob});
        }

        priority_queue<pair<double, int>> pq;
        pq.push({1.0, start_node});

        vector<double> max_prob(n, 0.0);
        max_prob[start_node] = 1.0;
        
        while (!pq.empty()){
            pair<double, int> cur = pq.top();
            pq.pop();

            double cur_prob = cur.first;
            int node = cur.second;
            
            if (node == end_node){
                return cur_prob;
            }
            for (const auto& neighbor: graph[node]){
                int nxt = neighbor.first;
                double nxt_prob = neighbor.second;
                double prob = cur_prob * nxt_prob;
                if (prob > max_prob[nxt]){
                    max_prob[nxt] = prob;
                    pq.push({prob, nxt});
                }
            }
        }
        return 0.0;
    }
};