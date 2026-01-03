# 矩阵乘法
# forked (https://leetcode.cn/problems/number-of-ways-to-paint-n-3-grid/solutions/3869310/san-chong-fang-fa-ji-yi-hua-sou-suo-di-t-tell)
# a的列数必须等于b的行数目
# a=m*n b=n*z a@b=m*z
def mul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


# 快速幂运算 m^n * origin
def pow_mul(m: list[list[int]], n: int, origin: list[list[int]]) -> list[list[int]]:
    res = origin
    while n:
        if n & 1:
            res = mul(m, res)
        m = mul(m, m)
        n >>= 1
    return res


if __name__ == "__main__":
    print(mul([[1, 2, 3], [4, 5, 6]], [[1], [2], [3]]))
    # [[14], [32]]

    print(pow_mul([[1, 2], [3, 4]], 2, [[1], [1]]))
