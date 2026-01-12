# 位运算

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
