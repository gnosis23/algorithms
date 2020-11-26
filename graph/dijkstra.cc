#include <list>
#include <vector>
#include <set>
using std::vector;
using std::list;
using std::pair;
using std::set;

typedef struct _Node {
    _Node(int s0,int e0,int w0):s(s0),e(e0),w(w0) {}
    int s,e,w;
} LNode;
typedef vector<list<LNode>> Edges;

void dijk(int n, int start, const Edges& edges, int *d) {
    set<pair<int,int>> st;
    for (int i = 0; i < n; ++i) d[i] = INT_MAX;
    st.insert({0, start});
    d[start] = 0;
    while (!st.empty()) {
        int s = st.begin()->second;
        st.erase(st.begin());
        for (const auto& edge : edges[s]) {
            if (d[s] + edge.w < d[edge.e]) {
                st.erase({d[edge.e], edge.e});
                d[edge.e] = d[s] + edge.w;
                st.insert({d[edge.e], edge.e});
            }
        }
    }
}
