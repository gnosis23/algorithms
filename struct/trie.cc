#include <string>

class Trie {
    const static int DICT_LEN = 26;
    struct Node {
        Node(): isValue(false) {}
        bool isValue;
        Node* nodes[DICT_LEN] = {};
        Node* get(int offset) { return nodes[offset]; }
    };
    Node* head;
public:
    /** Initialize your data structure here. */
    Trie() {
        head = new Node();
    }
    ~Trie() {
        release(head);
    }
    
    /** Inserts a word into the trie. */
    void insert(const std::string &word) {
        if (word.empty()) return;
        Node *ptr = head;
        for (char ch : word) {
            int index = offset(ch);
            if (ptr->nodes[index] == nullptr) {
                ptr->nodes[index] = new Node();
            }
            ptr = ptr->get(index);
        }
        ptr->isValue = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(const std::string &word) {
        Node *ptr = head;
        for (char ch : word) {
            int index = offset(ch);
            if (ptr->nodes[index] == nullptr) {
                return false;
            }
            ptr = ptr->get(index);
        }
        return ptr != nullptr && ptr->isValue;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(const std::string &prefix) {
        Node *ptr = head;
        for (char ch : prefix) {
            int index = offset(ch);
            if (ptr->nodes[index] == nullptr) {
                return false;
            }
            ptr = ptr->get(index);
        }
        return ptr != nullptr;
    }
private:
    inline int offset(char ch) {
        return ch - 'a';
    }
    void release(Node* node) {
        for (int i = 0; i != DICT_LEN; ++i) {
            if (node->nodes[i] != nullptr) {
                release(node->nodes[i]);
            }
        }
        delete node;
    }
};