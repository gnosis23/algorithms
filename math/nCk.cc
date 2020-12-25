typedef long long ll;

// 不能超过20
ll nCk(int n, int k) {
    if (n < k) return 0;
    if (n - k > k) k = n - k;
    ll i, j;
    ll s = 1;
    for (i = 0, j = 1; i < k; ++i) {
        s *= (n-i);
        for (; j <= k && (s % j == 0); ++j) s /= j;
    }
    return s;
}
