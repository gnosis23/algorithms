#include <vector>
using std::vector;
typedef long long ll;

/**
 * 线段树
 * 支持区间加法，区间求和
 * 根节点从0开始，区间左闭右开从0开始。
 */
class SegmentTree {
public:
    typedef ll vtype;    
    SegmentTree(int _size) {
        size = _size;
        int n = _size * 4;
        data = std::move(vector<vtype>(n, 0));
        sum = std::move(vector<vtype>(n, 0));
    }
    inline int lc(int k) { return (k<<1)|1; }
    inline int rc(int k) { return (k<<1)+2; }
    int size;
    vector<vtype> data;
    // lazy data
    vector<vtype> sum;
    // usage: build(data, 0, 0, n)
    void build(vtype *d, int k, int l, int r) {
        if(r - l < 2){	//	l + 1 == r
            data[k] = d[l];
            return;
        }
        int mid = (l + r) / 2;
        build(d, lc(k), l, mid);
        build(d, rc(k), mid, r);
        pushUp(k);
    }
    // usage: update(a, b, v, 0, 0, n)
    //  warn: [a,b] => [a-1, b)
    void update(int a, int b, vtype v, int k, int l, int r) {
        if (r <= a || b <= l) return;
        if (a <= l && r <= b) {
            data[k] += v * (r - l);
            sum[k] += v;
            return;
        }
        pushDown(k, l, r);
        int mid = (l + r) / 2;
        if (a<=mid) update(a, b, v, lc(k), l, mid);
        if (b>=mid) update(a, b, v, rc(k), mid, r);
        pushUp(k);
    }
    inline void foo(int k, int c, int l, int r) {
        sum[c] += sum[k];
        data[c] += sum[k] * (r - l);
    }
    inline void pushDown(int k, int l, int r) {
        int mid = (l + r) / 2;
        foo(k, lc(k), l, mid);
        foo(k, rc(k), mid, r);
        // clear lazy
        sum[k] = 0;
    }
    inline void pushUp(int k) {
        data[k] = data[lc(k)] + data[rc(k)];
    }
    // usage: query(a, b, 0, 0, n)
    //  warn: [a,b] => [a-1, b)
    vtype query(int a, int b, int k, int l, int r) {
        if (r <= a || b <= l) return 0;
        if (a <= l && r <= b) return data[k];
        else {
            pushDown(k, l, r);
            vtype res = 0;
            int mid = (l + r) / 2;
            if (a<=mid) res += query(a, b, lc(k), l, mid);
            if (b>=mid) res += query(a, b, rc(k), mid, r);
            return res;
        }
    }
};