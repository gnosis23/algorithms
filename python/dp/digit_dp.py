"""
数位DP
下面的例子求所有数字中包含1的个数
"""

from functools import cache


@cache
def dfs(n_str, pos, state, tight, valid):
    """
    pos: 当前处理到第几位（从高到低）
    state: 状态变量（如前一位数字、数字之和等，根据题意变化）
    tight: 布尔值，表示当前位是否受到上界限制
    valid: 布尔值，表示前几位是否填了数字（用于处理前导零）
    """
    if pos == len(n_str):
        # 判断是否满足条件
        return state if (valid) else 0

    res = 0
    up = int(n_str[pos]) if tight else 9

    for i in range(up + 1):
        if not valid and i == 0:
            # 依然处于前导零状态，不改变 state，pos 加 1
            res += dfs(n_str, pos + 1, state, tight and (i == up), False)
        else:
            # 更新状态
            new_state = state + 1 if (i == 1) else state
            res += dfs(n_str, pos + 1, new_state, tight and (i == up), True)

    return res


if __name__ == "__main__":
    dfs("123", 0, 0, True, False)
