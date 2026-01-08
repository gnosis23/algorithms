# 位运算技巧
n = 0b1110

# 获取最低位的1
lowbit = n & -n  # 0b10


def subsets(n):
    """倒序枚举非空子集 (不包括0)"""
    # 如果从n开始 sub = n
    sub = (n - 1) & n
    while sub > 0:
        print(bin(sub))
        sub = (sub - 1) & n


def lowbits_index(n):
    """获取n的低位1索引"""
    mask = n
    while mask > 0:
        lowbit = mask & -mask
        print(lowbit.bit_length() - 1)
        mask ^= lowbit
