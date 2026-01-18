# 单调栈

单调栈（Monotonic Stack） 是一种非常巧妙的数据结构应用，本质上是普通的栈，
但在入栈时通过特定的规则，始终保持栈内元素的单调性（递增或递减）。

它被誉为解决“**找左右第一个更大/更小元素**”这类问题的“银弹”。

## 基础

- [LC739. 每日温度](): 维护一个右侧的递增栈
- [LC1475. 商品折扣后的最终价格]():
- [LC3814. 预算下的最大总容量][1]: 维护前 i 个元素的最大价值 + 二分搜索

## 矩形

- [LC84. 柱状图中的最大的矩形](): 枚举左右两边最近的比自己小的元素位置
- [LC85. 最大矩形](): LC84 加强版；按行求最大矩形

## 最小字典序列

- [316. 去除重复字母 (2185)][2]: 移除重复的字母，使得返回的字符串尽量小
  - 对于重复的字符串，什么时候删除？存在下一个字符比他小的字符串，且他在后面还会出现
  - 维护一个栈
- [3816. 删除重复字符后的字典序最小的字符串][3]: 这个题目可以重复字符串
  - 对于重复的字符串，什么时候删除？存在下一个字符比他小的字符串，且他在后面还会出现or当前已经出现了>1次

[1]: https://leetcode.cn/problems/maximum-capacity-within-budget/description/
[2]: https://leetcode.cn/problems/remove-duplicate-letters/description/
[3]: https://leetcode.cn/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/description/
