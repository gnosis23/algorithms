#!/usr/bin/env python3
"""
Binary Indexed Tree (Fenwick Tree) 测试
"""

import sys

# 导入 BinaryIndexedTree 类，但不执行 bit.py 的 main()
import bit

BinaryIndexedTree = bit.BinaryIndexedTree


def test_basic_operations():
    """测试基本操作"""
    bit = BinaryIndexedTree(5)

    # 添加元素
    bit.add(0, 5)
    bit.add(1, 3)
    bit.add(2, 7)
    bit.add(3, 2)
    bit.add(4, 8)

    # 测试前缀和
    assert bit.sum(0) == 5  # [0,0] = 5
    assert bit.sum(1) == 8  # [0,1] = 5+3 = 8
    assert bit.sum(2) == 15  # [0,2] = 5+3+7 = 15
    assert bit.sum(3) == 17  # [0,3] = 5+3+7+2 = 17
    assert bit.sum(4) == 25  # [0,4] = 5+3+7+2+8 = 25


def test_update_operations():
    """测试更新操作"""
    bit = BinaryIndexedTree(5)

    # 初始添加
    bit.add(0, 5)
    bit.add(1, 3)
    bit.add(2, 7)
    bit.add(3, 2)
    bit.add(4, 8)

    # 更新元素
    bit.add(0, -1)  # 5 -> 4
    bit.add(2, 3)  # 7 -> 10

    # 测试更新后的前缀和
    assert bit.sum(0) == 4  # [0,0] = 4
    assert bit.sum(1) == 7  # [0,1] = 4+3 = 7
    assert bit.sum(2) == 17  # [0,2] = 4+3+10 = 17
    assert bit.sum(3) == 19  # [0,3] = 4+3+10+2 = 19
    assert bit.sum(4) == 27  # [0,4] = 4+3+10+2+8 = 27


def test_edge_cases():
    """测试边界情况"""
    # 测试大小为1的树
    bit1 = BinaryIndexedTree(1)
    bit1.add(0, 10)
    assert bit1.sum(0) == 10

    # 测试大小为0的树
    bit0 = BinaryIndexedTree(0)
    # 对于大小为0的树，add操作应该被忽略或失败
    # 这里我们只测试它不会崩溃

    # 测试负值添加
    bit = BinaryIndexedTree(3)
    bit.add(0, 10)
    bit.add(1, -5)
    bit.add(2, 3)

    assert bit.sum(0) == 10  # [0,0] = 10
    assert bit.sum(1) == 5  # [0,1] = 10 + (-5) = 5
    assert bit.sum(2) == 8  # [0,2] = 5 + 3 = 8


def test_range_queries():
    """测试区间查询（通过前缀和计算）"""
    bit = BinaryIndexedTree(10)

    # 添加一些数据: 1, 2, 3, ..., 10
    for i in range(10):
        bit.add(i, i + 1)

    # 测试区间和 [l, r] = sum(r) - sum(l-1)
    def range_sum(l, r):
        if l == 0:
            return bit.sum(r)
        return bit.sum(r) - bit.sum(l - 1)

    # 测试几个区间
    assert range_sum(0, 0) == 1  # [0,0] = 1
    assert range_sum(0, 4) == 15  # [0,4] = 1+2+3+4+5 = 15
    assert range_sum(2, 5) == 18  # [2,5] = 3+4+5+6 = 18
    assert range_sum(5, 9) == 40  # [5,9] = 6+7+8+9+10 = 40


def test_large_array():
    """测试大数组性能"""
    n = 1000
    bit = BinaryIndexedTree(n)

    # 添加数据: 1, 2, 3, ..., 1000
    for i in range(n):
        bit.add(i, i + 1)

    # 验证总和: 1+2+...+1000 = 1000*1001/2 = 500500
    expected_total = n * (n + 1) // 2
    assert bit.sum(n - 1) == expected_total

    # 随机更新和查询
    bit.add(500, 100)  # 增加第501个元素100 (原值501 -> 601)

    # 验证更新后的前缀和
    # sum(500) = (1+2+...+500) + 100 = 500*501/2 + 100 = 125250 + 100 = 125350
    expected_sum_500 = (
        500 * 501 // 2 + 100 + 501
    )  # 注意：第501个元素本身是501，加上100后是601
    # 修正：sum(500) 包含前501个元素的和
    # 前500个元素和：500*501/2 = 125250
    # 第501个元素：501 + 100 = 601
    # 总和：125250 + 601 = 125851
    expected_sum_500 = 500 * 501 // 2 + 501 + 100
    assert bit.sum(500) == expected_sum_500


def main():
    """运行所有测试"""
    tests = [
        ("基本操作", test_basic_operations),
        ("更新操作", test_update_operations),
        ("边界情况", test_edge_cases),
        ("区间查询", test_range_queries),
        ("大数组", test_large_array),
    ]

    passed = 0
    failed = 0

    for name, test_func in tests:
        try:
            test_func()
            print(f"✓ {name}测试通过")
            passed += 1
        except AssertionError as e:
            print(f"✗ {name}测试失败: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {name}测试错误: {e}")
            failed += 1

    print(f"\n总计: {passed}通过, {failed}失败")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
