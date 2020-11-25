#include <list>
#include <queue>
#include <vector>
using std::vector;
using std::list;
using std::priority_queue;

typedef struct _Node {
    _Node(int s0,int e0,int w0):s(s0),e(e0),w(w0) {}
    int s,e,w;
} LNode;
typedef vector<list<LNode>> Edges;

struct DijkstraNodeComparator {
    bool operator()(const LNode& a, const LNode& b) {
        return a.w > b.w;
    }
};

void dijk(int n, int start, const Edges& edges, int *d) {
    priority_queue<LNode, vector<LNode>, DijkstraNodeComparator> pq;
    vector<bool> found(n, false);
    pq.push(LNode(start, start, 0));
    while (!pq.empty()) {
        LNode next = pq.top();
        pq.pop();
        if (found[next.e]) continue;
        found[next.e] = true;
        d[next.e] = next.w;
        for (const auto& edge : edges[next.e]) {
            if (!found[edge.e]) {
                pq.push(LNode(0, edge.e, d[next.e] + edge.w));
            }
        }
    }
}
