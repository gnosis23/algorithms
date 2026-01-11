# 位运算

## 试填法

- [LC3806. 增加操作后最大按位与的结果][1]: 任取 m 个，加 k 次求最大的与
  - 从高位到低位枚举 1，如果 k 还有剩余，继续枚举
  - 贪心取前 m 小的代价

[1]: https://leetcode.cn/problems/maximum-bitwise-and-after-increment-operations/description/
