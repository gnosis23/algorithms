# 二分算法

## 二分搜索

- [LC35. 搜索插入位置][2]: == bisect_left
- [LC704. 二分查找][3]
  - bisect_left 返回为长度则-1，或者返回 pos 也不一定是结果
- [LC3814. 预算下的最大总容量][1]
  - 在前缀最大值的前面加一个哨兵 0，这样 bisect_left 结果 -1 就是最大值

[1]: https://leetcode.cn/problems/maximum-capacity-within-budget/description/
[2]: https://leetcode.cn/problems/search-insert-position/description/
[3]: https://leetcode.cn/problems/binary-search/description/
