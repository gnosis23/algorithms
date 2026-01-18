"""
求：给定 nums 数组和整数 k，求和为 k 的子数组的个数；子数组不能为空；k可以为负数
解：
从数组下标 i = 0 开始迭代，逐个统计所有数和=prefix
令 cnt[x] 为前缀和为 x 的数量，那么只要存在 cnt[prefix - k] > 0
就能形成几个子数组和为 k = prefix - (prefix - k)

举个例子：nums = [1, 1, 2, 3]，k = 3
i = 0, prefix = 1, cnt = {0:1, 1:1}
i = 1, prefix = 2, cnt = {0:1, 1:1, 2:1}
i = 3, prefix = 4, cnt = {0:1, 1:1, 2:1, 4:1},
    此处 cnt[prefix - k] = cnt[1] > 0，结果+=cnt[1]
i = 4, prefix = 7, cnt = {0:1, 1:1, 2:1, 4:1, 7:1}
    此处 cnt[prefix - k] = cnt[4] > 0, 结果+=cnt[4]

举个例子：nums = [1, 1, 1]，k = 2
i = 0, prefix = 1, cnt = {0:1, 1:1}
i = 1, prefix = 2, cnt = {0:1, 1:1, 2:1}
    此处 cnt[prefix - k] = cnt[0] > 0
i = 2, prefix = 3, cnt = {0:2, 1:1, 2:1, 3:1}
    此处 cnt[prefix - k] = cnt[1] > 0

初始化 cnt[0] = 1
"""

from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        cnt[0] = 1
        prefix = 0
        ans = 0
        for i in range(n):
            prefix = prefix + nums[i]
            ans += cnt[prefix - k]
            cnt[prefix] += 1
        return ans
