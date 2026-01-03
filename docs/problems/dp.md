# DP

## 数位 DP

数位 DP (Digit Dynamic Programming) 是一种特殊的动态规划技巧，主要用于解决在给定区间 $[L, R]$ 内，
统计满足特定条件的整数个数的问题。

这类问题的特点是：题目给出的范围通常极大（如 $10^{18}$ 或更大），直接暴力遍历必然超时，
而数位 DP 通过将数字拆分为每一位，利用记忆化搜索来高效求解。

- [3791. 给定范围内平衡整数的数目][1]

## References

[1]: https://leetcode.cn/problems/number-of-balanced-integers-in-a-range/description/
