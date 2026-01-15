# DS

## 树状数组

- [LC307. 区域和检索 - 数组可修改][1]
- [LC3072. 将元素分配到两个数组中 II (2052)][2]: 求一个数组中 >= x_i 的数量
  - 离散化以后转为统计区间和
- [LC3624. 位计数深度为 K 的整数数目 II (2086)][3]: 求一个数组中 f(x_i) == K 的数量
  - K 的范围是 0~5 ，用 6 个树状数组

## 线段树

- [LC3479. 水果成篮 III (2178)][4]: 查找第一个满足>=k 的位置。模板
- [LC2940. 找到 Alice 和 Bob 相遇的建筑 (2327)][5]: 同上

## Lazy 线段树

- [LC2569. 更新数组后处理求和查询 (2398)][8]: `nums2[i] = nums2[i] + nums1[i] * p`
  - 不用管 nums2 ；操作一 == apply(-1, 1)；操作二 == apply(p, 0)
- [LC1622. 奇妙序列][9]: `nums[i] = a*x + b`
  - Python 超时，C++过来
- [LC850. 矩形面积 II][7]: 扫描线，离散化，线段树
- [LC3454. 分割正方形 II (2671)][6]

## Reference

- [树状数组](https://oi-wiki.org/ds/fenwick)

[1]: https://leetcode.cn/problems/range-sum-query-mutable/
[2]: https://leetcode.cn/problems/distribute-elements-into-two-arrays-ii/description/
[3]: https://leetcode.cn/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/description/
[4]: https://leetcode.cn/problems/fruits-into-baskets-iii/description/
[5]: https://leetcode.cn/problems/find-building-where-alice-and-bob-can-meet/description/
[6]: https://leetcode.cn/problems/separate-squares-ii/description/
[7]: https://leetcode.cn/problems/rectangle-area-ii/description/
[8]: https://leetcode.cn/problems/handling-sum-queries-after-update/description/
[9]: https://leetcode.cn/problems/fancy-sequence/description/
