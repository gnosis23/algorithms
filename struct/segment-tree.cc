#include <vector>
using std::vector;
#define long long ll;

class SegmentTree {
public:
    typedef ll vtype;
    SegmentTree(int _size) {
        size = _size;
        int n = 1;
        while (n < _size) n *= 2;
        n = 2 * n;
        data = std::move(vector<vtype>(n, 0));
    }
    void build(vtype *d) {
        _build(d, 0, 0, size);
    }
    // offset-1, [a, b]
    void update(int a, int b, vtype v) {
        _update(a, b+1, v, 0, 0, size);
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
    vtype _update(int a, int b, vtype v, int k, int l, int r) {
        if (r <= a || b <= l) return 0;
        if (r - l < 2) {
            data[k] += v;
            return v;
        }
        vtype v1 = _update(a, b, v, k * 2 + 1, l, (l + r)/2);
        vtype v2 = _update(a, b, v, k * 2 + 2, (l + r)/2, r);
        vtype val = v1 + v2;
        data[k] += val;
        return val;
    }    
    // usage: query(a, b, 0, 0, n)
    vtype _query(int a, int b, int k, int l, int r) {
        if (r <= a || b <= l) return 0;
        if (a <= l && r <= b) return data[k];
        else {
            vtype vl = _query(a, b, k * 2 + 1, l, (l + r)/2);
            vtype vr = _query(a, b, k * 2 + 2, (l + r)/2, r);
            return vl + vr;
        }
    }
    vector<vtype> data;
    int size;
};