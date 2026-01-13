# 位运算

## 拆位/贡献法

在算法竞赛和高级编程中，“拆位 (Bitwise Decomposition)” 与 “贡献法 (Contribution Technique)” 是处理位运算问题的核心组合拳。

简单来说，当题目要求你计算一个数组中所有元素两两之间（或子数组/子集）的某种位运算结果之和时，直接模拟通常是 $O(N^2)$，
而“拆位 + 贡献法”能将其优化到 $O(N \cdot \log(\text{max\_val}))$。

拆位 (Bitwise Decomposition) 核心思想：位与位之间是独立的。在位运算（如 & AND, | OR, ^ XOR）中，
第 $i$ 位的计算结果只取决于参与运算数字的第 $i$ 位，与第 $i+1$ 位或第 $i-1$ 位无关（没有进位）。

贡献法 (Contribution Technique)核心思想：与其计算每个组合的结果，不如计算每个元素/每一位被计算了多少次。
当我们把问题拆解到“第 $i$ 位”时，这一位上的值只有 $0$ 或 $1$。此时，我们只需要统计：
有多少种组合方式能让这一位的结果为 $1$？

- [LC477. 汉明距离总和][4]
- [LC1863. 找出所有子集的异或总和再求和][5]
  - 对于每一位来说，要想异或结果为 1，需要奇数个 1
  - ~~对于第 d 位来说，和就是 `(C(cnt1, 1) + C(cnt1, 3) + ...) * 2^cnt0 * (1 << (d - 1))`~~
  - 对于某一位上如果有 1，异或和为 1 的子集个数就是 2^(n-1)，和 1 的数量无关

## 试填法

从高位到低位枚举值，如果某位不满足则跳过。

- [LC421. 数组中两个数的最大异或值][2]
  - a^b=m, a^m=b
  - 从高位到低位枚举，如果元素 i 的异或结果存在于 nums 集合，说明这一位是合理的
- [LC2935. 找出强数对的最大异或值][3]: 上面一道题的加强版
  - 在集合里存储 `nums[i]`，并验证是否满足强数
- [LC3806. 增加操作后最大按位与的结果][1]: 任取 m 个，加 k 次求最大的与
  - 从高位到低位枚举 1，如果 k 还有剩余，继续枚举
  - 贪心取前 m 小的代价

[1]: https://leetcode.cn/problems/maximum-bitwise-and-after-increment-operations/description/
[2]: https://leetcode.cn/problems/maximum-xor-of-two-numbers-in-an-array/description/
[3]: https://leetcode.cn/problems/maximum-strong-pair-xor-ii/description/
[4]: https://leetcode.cn/problems/total-hamming-distance/description/
[5]: https://leetcode.cn/problems/sum-of-all-subset-xor-totals/
