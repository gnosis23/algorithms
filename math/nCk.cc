typedef long long ll;

// caution: overflow
ll nCk(int n, int k) {
    ll s = 1;
    for (ll d = 1; d <= k; ++d) {
        s *= n--;
        s /= d;
    }
    return s;
}