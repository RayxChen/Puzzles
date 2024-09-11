#include <unordered_map>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = nullptr;
        random = nullptr;
    }
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*> CopyMap;
        Node* cur = head;
        while (cur){
            CopyMap[cur] = new Node(cur->val);
            cur = cur->next;
        }
        cur = head;

        while (cur){
            Node* clone = CopyMap[cur];
            if (cur->next){
                clone->next = CopyMap[cur->next];
            }
            if (cur->random){
                clone->random = CopyMap[cur->random];
            }
            cur = cur->next;
        }
        return CopyMap[head];
         
    }
    
    void deleteList(Node* head) {
        Node* temp = nullptr;
        while (head) {
            temp = head;
            head = head->next;
            delete temp;  // Delete the node to free memory
        }
    }
};