typedef long long ll;

/**
 * 拓展欧几里得
 * a*x + b*y = gcd(a, b)
 * x,y 可能为负数
 */
ll extgcd(ll a, ll b, ll &x, ll &y) {
    ll d = a;
    if (b != 0) {
        d = extgcd(b, a % b, y, x);
        y -= (a / b) * x;
    } else {
        x = 1; y = 0;
    }
    return d;
}

/**
 * 求最小解 ax = b (mod n)
 */
ll modeq(ll a, ll b, ll n) {
    ll e, i, d, x, y;
    d = extgcd(a, n, x, y);
    if (b % d > 0) {
        return -1;
    }
    else {
        e = (x * (b / d)) % n;
        // for (int i = 0; i < d; ++i) {
        //   ans = (e + i * (n/d) + n) % n;
        // }
        ll ans = ((e + n) % (n/d)) %n;
        return ans;
    }
}

/**
 * 求解逆元
 */
ll mod_inverse(ll a, ll m) {
    ll x, y;
    extgcd(a, m, x, y);
    return (m + x % m) % m;
}
