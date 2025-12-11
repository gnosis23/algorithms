#include <vector>
using std::vector;

/**
 * 带路径压缩的并查集
 **/
class DisjointSet {
public:
    DisjointSet(int n){
        p = vector<int>(n + 1);
        rank = vector<int>(n + 1);
        for (int i = 0; i <= n; ++i) {
            p[i] = i;
            rank[i] = 0;
        }
    }
    bool inSame(int u, int v) {
        return findSet(u) == findSet(v);
    }
    void join(int u, int v) {
        if (findSet(u) != findSet(v)) {
            link(findSet(u), findSet(v));
        }
    }
    int findSet(int u) {
        if (u != p[u]) {
            p[u] = findSet(p[u]);
        }
        return p[u];
    }
private:
    vector<int> p;
    vector<int> rank;
    void link(int u, int v) {
        if (rank[u] > rank[v]) {
            p[v] = u;
        } else {
            p[u] = v;
            if (rank[u] == rank[v]) {
                rank[u] = rank[v] + 1;
            }
        }
    }
};
