def get_primes(up: int) -> list[int]:
    """
    线性筛素数法（欧拉筛 Sieve of Euler）
    """
    vis = [False] * (up + 1)
    primes = []
    for i in range(2, up + 1):
        if not vis[i]:
            primes.append(i)

        for p in primes:
            if p * i <= up:
                vis[p * i] = True
                # 核心：保证每个合数只被其最小质因子筛去
                if i % p == 0:
                    break
            else:
                break
    return primes


def factorize_with_primes(n, primes):
    """整数分解因数"""
    factors = {}
    temp = n

    for p in primes:
        # 优化核心：如果当前素数的平方大于剩余待分解的数，剩下的就是质数
        if p * p > temp:
            break

        if temp % p == 0:
            count = 0
            while temp % p == 0:
                count += 1
                temp //= p
            factors[p] = count

    # 最后剩下的 temp 如果大于 1，说明它是一个比所有测试过的素数都大的质数
    if temp > 1:
        factors[temp] = 1

    return factors


if __name__ == "__main__":
    print(get_primes(1000))
    primes = get_primes(100000)
    print(len(primes))
    print(factorize_with_primes(12248, primes))
    print(factorize_with_primes(11117, primes))
