# 位运算技巧
n = 0b1110

# 获取最低位的1
lowbit = n & -n  # 0b10

# 倒序枚举子集
sub = (n - 1) & n
while sub > 0:
    print(bin(sub))
    sub = (sub - 1) & n
# 0b1100
# 0b1000
# 0b100
