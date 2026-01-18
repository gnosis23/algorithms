# 二分算法

## 二分搜索

二分索引：

- 模式1: `>= x` 的第一个元素的下标: bisect_left(nums, x)，不存在则为 n
- 模式2: `>  x` 的第一个元素的下标: bisect_right(nums, x)，不存在则为 n
- 模式3: `<= x` 的最后一个元素的下标: bisect_right(nums, x) - 1，不存在则为 -1
- 模式4: `<  x` 的最后一个元素的下标: bisect_left(nums, x) - 1，不存在则为 -1

统计数字：

- `>= x` 的元素个数：n - bisect_left(nums, x)
- `>  x` 的元素个数: n - bisect_right(nums, x)
- `<= x` 的元素个数：bisect_right(nums, x)
- `<  x` 的元素个数：bisect_left(nums, x)
- `== x` 的元素个数：bisect_right(nums, x) - bisect_left(nums, x)
- 在 `[low, high]` 中 `== x` 的元素个数：bisect_right(nums, x, lo=low, high=high+1) - bisect_left(nums, x, lo=low, high=high+1)

### 基础

- [LC34. 在排序数组中查找元素的第一个和最后一个位置][4]: 练习 bisect_left 和 bisect_right
  - 注意 `bisect_right` 指向下一个位置
- [LC35. 搜索插入位置][2]: == bisect_left
- [LC704. 二分查找][3]
  - bisect_left 返回 == n 则 -1，还需要判断是否==target
- [LC3814. 预算下的最大总容量][1]
  - 在前缀最大值的前面加一个哨兵 0，这样 bisect_left 结果 -1 就是最大值
- [LC2529. 正整数和负整数的最大计数][5]

### 进阶

- [LC1385. 两个数组间的距离值 (1235)][6]: 求得索引区间，判断是否相交
- [LC2389. 和有限的最长子序列][7]: 模式3
- [LC2080. 区间内查询数字的频率][8]: 同1385

[1]: https://leetcode.cn/problems/maximum-capacity-within-budget/description/
[2]: https://leetcode.cn/problems/search-insert-position/description/
[3]: https://leetcode.cn/problems/binary-search/description/
[4]: https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/
[5]: https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer/
[6]: https://leetcode.cn/problems/find-the-distance-value-between-two-arrays/description/
[7]: https://leetcode.cn/problems/longest-subsequence-with-limited-sum/description/
[8]: https://leetcode.cn/problems/range-frequency-queries/description/
