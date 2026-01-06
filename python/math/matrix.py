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


def infer_matrix(n, transformation):
    """
    倒推矩阵：提供n-纬度和transformation-线性向量变换函数，得到 n*n 的矩阵
    假设递推公式 f(n) = 5 * f(n - 1) - 2 * f(n - 2)
    现在需要构造 [f(n), f(n - 1)] = M * [f(n - 1), f(n - 2)] 里面的 M 矩阵
    可以使用 n=2, transformation = lambda x: (5 * x[0] - 2 * x[1], x[0])
    可以求出矩阵 ((5, -2), (1, 0))
    transformation(1,0,0...) => 矩阵第1列
    transformation(0,1,0...) => 矩阵第2列
    transformation(0,0,1...) => 矩阵第n列
    """

    def one_hot(n, i):
        vertex = [0] * n
        vertex[i] = 1
        return tuple(vertex)

    cols = [transformation(one_hot(n, i)) for i in range(n)]
    return tuple(zip(*cols))


if __name__ == "__main__":
    print(mul([[1, 2, 3], [4, 5, 6]], [[1], [2], [3]]))
    # [[14], [32]]

    print(pow_mul([[1, 2], [3, 4]], 2, [[1], [1]]))

    print(infer_matrix(2, lambda x: (5 * x[0] - 2 * x[1], x[0])))
