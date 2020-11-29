#include <vector>
using std::vector;
#define long long ll;

class SegmentTree {
public:
    typedef ll vtype;
    SegmentTree(int _size) {
        size = _size;
        int n = _size * 4;
        data = std::move(vector<vtype>(n, 0));
        delta = std::move(vector<vtype>(n, 0));
    }
    void build(vtype *d) {
        _build(d, 0, 0, size);
        dumpArray(&data[0], data.size());
    }
    // offset-1, [a, b]
    void update(int a, int b, vtype v) {
        _update(a, b+1, v, 0, 0, size);
        // dumpArray(&data[0], data.size());
    }
    // offset-1, [a, b]
    vtype query(int a, int b) {
        return _query(a, b+1, 0, 0, size);
    }
private:
    // k >= 0, [l, r)
    void _build(vtype *d, int k, int l, int r) {
        if(r - l < 2){	//	l + 1 == r
            data[k] = d[l];
            return;
        }
        int mid = (l + r) / 2;
        _build(d, k * 2 + 1, l, mid);
        _build(d, k * 2 + 2, mid, r);
        data[k] = data[k * 2 + 1] + data[k * 2 + 2];
    }
    // usage: update(a, b, v, 0, 0, n)
    void _update(int a, int b, vtype v, int k, int l, int r) {
        if (r <= a || b <= l) return;
        if (a <= l && r <= b) {
            data[k] += v * (r - l);
            delta[k] += v;
            return;
        }
        pushDown(k, l, r);
        int mid = (l + r) / 2;
        if (a<=mid) _update(a, b, v, k * 2 + 1, l, mid);
        if (b>=mid) _update(a, b, v, k * 2 + 2, mid, r);
        pushUp(k);
    }
    // usage: query(a, b, 0, 0, n)
    vtype _query(int a, int b, int k, int l, int r) {
        if (r <= a || b <= l) return 0;
        if (a <= l && r <= b) return data[k];
        else {
            pushDown(k, l, r);
            ll res = 0;
            int mid = (l + r) / 2;
            if (a<=mid) res += _query(a, b, k * 2 + 1, l, mid);
            if (b>=mid) res += _query(a, b, k * 2 + 2, mid, r);
            return res;
        }
    }
    inline void pushDown(int k, int l, int r) {
        int mid = (l + r) / 2;
        delta[k*2+1] += delta[k];
        data[k*2+1] += delta[k] * (mid - l);
        delta[k*2+2] += delta[k];
        data[k*2+2] += delta[k] * (r - mid);
        delta[k] = 0;
    }
    inline void pushUp(int k) {
        data[k] = data[k*2+1] + data[k*2+2];
    }
    vector<vtype> data;
    vector<vtype> delta;
    int size;
};
