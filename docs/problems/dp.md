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

## 状态压缩

用 `dp[s]` 表示状态，s 为 n 个*已选*元素的集合(大小 2^n) 。 n 一般 <= 15

### 排列

把 n 个元素放到 k 个地方

- LC526. 优美的排列: `dp[s]` 记录排列的数量
- LC3376. 破解锁的最少时间 I: `dp[s]` 记录开锁的最少时间。更新和集合大小有关
- LC1879. 两个数组最小的异或值之和
- LC2850. 将石头分散到网络图的最少移动次数: `dp[s]` 为将 n 个石头移动到 0 的最小次数，n 最大为 8

### 排列++

把 n 个元素放到 k 个地方，需要记录额外的状态

- [LC2741. 特别的排列][9]: 统计排列数量，`dp[s][i]` 需要记录最后一位
- [LC996. 平方数组的数目][10]: 思路同上。注意重复数字需要在同一个迭代时跳过
- LC1681. 最小不兼容: `dp[s]` 选择 s 后最小和；预处理所有 k 个分组；每个状态枚举分组

### 状态压缩子集

通过枚举状态的子集进行状态迁移，一般通过 bit 表示集合。

枚举 k 个 bit 的所有状态的子集的时间复杂度是 `O(3^k)` 。k 一般 <= 15

- [LC2305. 公平分发饼干][7]
- [LC1986. 完成任务的最少工作时间段][8]
- LC1681. 最小不兼容
- [LC3801. 合并有序列表的最小成本][6]

## 前缀和优化

通过前缀相减获得一个区间的值，如 `values(i, j) = values(i) - values(j - 1)`

- LC1871. 跳跃游戏 VII: 如果 `[i - max, i - min]` 区间存在 0，则可以跳过去

## References

[1]: https://leetcode.cn/problems/number-of-balanced-integers-in-a-range/description/
[2]: https://leetcode.cn/problems/number-of-digit-one/description/
[3]: https://leetcode.cn/problems/count-distinct-integers-after-removing-zeros/
[4]: https://leetcode.cn/problems/count-of-integers/
[5]: https://leetcode.cn/problems/max-dot-product-of-two-subsequences
[6]: https://leetcode.cn/problems/minimum-cost-to-merge-sorted-lists/description/
[7]: https://leetcode.cn/problems/fair-distribution-of-cookies/description/
[8]: https://leetcode.cn/problems/minimum-number-of-work-sessions-to-finish-the-tasks/description/
[9]: https://leetcode.cn/problems/special-permutations/description/
[10]: https://leetcode.cn/problems/number-of-squareful-arrays/description/
