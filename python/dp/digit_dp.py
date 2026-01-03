"""
数位DP
下面的例子求奇偶位和为0
"""

from functools import cache


@cache
def dfs(n_str, pos, diff, is_limit, is_num):
    """
    pos: 当前处理到第几位（从高到低）
    state: 状态变量（如前一位数字、数字之和等，根据题意变化）
    is_limit: 布尔值，表示当前位是否受到上界限制
    is_num: 布尔值，表示前几位是否填了数字（用于处理前导零）
    """
    if pos == len(n_str):
        return 1 if (is_num and diff == 0) else 0

    res = 0
    # 确定当前位可以填写的数字范围
    up = int(n_str[pos]) if is_limit else 9

    for i in range(up + 1):
        # 处理前导零
        if not is_num and i == 0:
            # 依然处于前导零状态，不改变 diff，pos 加 1
            res += dfs(n_str, pos + 1, diff, is_limit and (i == up), False)
        else:
            # 正常填入数字
            new_diff = diff + i if (pos % 2 == 0) else diff - i
            res += dfs(n_str, pos + 1, new_diff, is_limit and (i == up), True)

    return res


if __name__ == "__main__":
    dfs("123", 0, 0, True, False)
