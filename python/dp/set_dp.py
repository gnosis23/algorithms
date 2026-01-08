"""
子集状压 DP
下面的题目是 LC3801 合并链表最小代价
"""


class Solution:
    def minMergeCost(self, lists: list[list[int]]) -> int:
        n = len(lists)

        # 预处理
        state_info = {}  # mask -> (median, sorted_list)

        for i in range(n):
            state_info[1 << i] = (lists[i][(len(lists[i]) - 1) // 2], lists[i])

        # 预处理中位数
        for mask in range(1, 1 << n):
            if mask not in state_info:
                # 找到最低位
                lowbit = mask & -mask
                prev_mask = mask ^ lowbit
                i = (lowbit).bit_length() - 1

                _, prev_list = state_info[prev_mask]
                curr_list = sorted(prev_list + lists[i])
                median = curr_list[(len(curr_list) - 1) // 2]
                state_info[mask] = (median, curr_list)

        inf = 1e20
        dp = [inf] * (1 << n)

        for i in range(n):
            dp[1 << i] = 0

        for mask in range(1, 1 << n):
            if bin(mask).count("1") < 2:
                continue

            # 高效枚举所有非空子集
            sub = (mask - 1) & mask
            while sub > 0:
                median1, list1 = state_info[sub]
                median2, list2 = state_info[mask ^ sub]
                value = len(list1) + len(list2) + abs(median1 - median2)
                dp[mask] = min(dp[mask], dp[sub] + dp[mask ^ sub] + value)
                sub = (sub - 1) & mask

        return dp[(1 << n) - 1]
