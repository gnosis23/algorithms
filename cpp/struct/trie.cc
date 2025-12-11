/**
 * Trie
 * 注意太大要放在全局
 * maxnode参考：最大长度 2^(L)-1
 * 
 */
#include <cstring>

template <size_t maxnode = 100, size_t sigma_size = 26>
class Trie {
public:
    int ch[maxnode][sigma_size];
    int val[maxnode];
    int sz;
    Trie() { sz = 1; memset(ch[0], 0, sizeof(ch[0])); }
    inline int idx(char c) { return c - 'a'; }
    void insert(char *s, int v) {
        int u = 0, n = strlen(s);
        for(int i = 0; i < n; ++i) {
            int c = idx(s[i]);
            if (!ch[u][c]) {
                memset(ch[sz], 0, sizeof(ch[sz]));
                val[sz] = 0;
                ch[u][c] = sz++;
            }
            u = ch[u][c];
        }
        val[u] = v;
    }
    int find(char *s) {
        int u = 0, n = strlen(s);
        for(int i = 0; i < n; ++i) {
            int c = idx(s[i]);
            if (!ch[u][c]) {
                return -1;
            }
            u = ch[u][c];
        }
        return val[u];
    }
};