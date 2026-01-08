# DP

## 最长公共子序列 LCS

- [LC1458: 两个子序列的最大点积][5]

## 数位 DP

数位 DP (Digit Dynamic Programming) 是一种特殊的动态规划技巧，主要用于解决在给定区间 $[L, R]$ 内，
统计满足特定条件的整数个数的问题。

这类问题的特点是：题目给出的范围通常极大（如 $10^{18}$ 或更大），直接暴力遍历必然超时，
而数位 DP 通过将数字拆分为每一位，利用记忆化搜索来高效求解。

为什么数位 DP 这么快？比如计算数字 1XXXX 和 2XXXX 的计算，其实后面部分是重复的，利用记忆化搜索可以
减少大量计算。时间复杂度=`O(K * State * 2 * 2)`

- [LC233. 数字 1 的个数][2]
- [LC3747. 统计移除零后不同整数的数目][3]
- [LC2719. 统计整数数目][4]
- [LC3791. 给定范围内平衡整数的数目][1]

## References

[1]: https://leetcode.cn/problems/number-of-balanced-integers-in-a-range/description/
[2]: https://leetcode.cn/problems/number-of-digit-one/description/
[3]: https://leetcode.cn/problems/count-distinct-integers-after-removing-zeros/
[4]: https://leetcode.cn/problems/count-of-integers/
[5]: https://leetcode.cn/problems/max-dot-product-of-two-subsequences
