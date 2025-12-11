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

ll nPk(int n, int k) {
    ll s = 1;
    for (ll d = 1; d <= k; ++d) {
        s *= n--;
    }
    return s;
}

ll factorial(int n) {
    ll r = 1;
    for (int i = 1; i <= n; i++) r *= i;
    return r;
}
