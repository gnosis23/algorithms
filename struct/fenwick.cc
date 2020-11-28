#include <vector>
using std::vector

class FenWick {
public:
    FenWick(int n): a(vector<int>(n+1,0)) {}
    // from index 1...x
    int sum(int x) {
        int sum = 0;
        while (x > 0)
            sum += a[x], x -= lsb(x);
        return sum;
    }
    void add(int x, int k) {
        int size = a.size() - 1;
        while (x <= size) 
            a[x] += k, x += lsb(x);
    }
private:
    inline int lsb(int x) { return x & (-x); }
    vector<int> a;
};
