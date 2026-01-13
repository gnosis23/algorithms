"""
数位DP：统计波峰和波谷的和
需要额外的状态值
"""

from functools import cache


@cache
def dfs(n_str, pos, state, pre, cmp, tight, valid):
    if pos == len(n_str):
        # 判断是否满足条件
        return state if (valid) else 0

    res = 0
    up = int(n_str[pos]) if tight else 9

    for i in range(up + 1):
        if not valid and i == 0:
            # 依然处于前导零状态，不改变 state，pos 加 1
            res += dfs(n_str, pos + 1, state, pre, cmp, tight and (i == up), False)
        else:
            # 更新状态
            new_state = state
            # 0=bad 1=gt 2=lt
            new_cmp = 0
            # 排除前导零
            if valid:
                if pre > i:
                    new_cmp = 1
                    if cmp == 2:
                        new_state += 1
                elif pre < i:
                    new_cmp = 2
                    if cmp == 1:
                        new_state += 1

            res += dfs(n_str, pos + 1, new_state, i, new_cmp, tight and (i == up), True)

    return res
