#!/usr/bin/env python3
"""
并查集 (Disjoint Set) 测试
"""

# 导入 DisjointSet 类，但不执行 disjoint-set.py 的 main()
import disjointset

DisjointSet = disjointset.DisjointSet


def test_initialization():
    """测试初始化"""
    n = 5
    ds = DisjointSet(n)

    # 每个元素应该是自己的父节点
    for i in range(n):
        assert ds.find_set(i) == i, f"元素 {i} 的根应该是自己"

    # 初始时所有元素都不在同一集合
    for i in range(n):
        for j in range(i + 1, n):
            assert not ds.in_same(i, j), f"初始时 {i} 和 {j} 不应该在同一集合"


def test_basic_union_find():
    """测试基本的合并和查找"""
    ds = DisjointSet(10)

    # 合并 0, 1, 2
    ds.join(0, 1)
    ds.join(1, 2)

    # 验证它们在同一集合
    assert ds.in_same(0, 1), "0 和 1 应该在同一个集合"
    assert ds.in_same(1, 2), "1 和 2 应该在同一个集合"
    assert ds.in_same(0, 2), "0 和 2 应该在同一个集合"

    # 合并 3, 4
    ds.join(3, 4)

    # 验证 3,4 在同一集合，但和 0,1,2 不在
    assert ds.in_same(3, 4), "3 和 4 应该在同一个集合"
    assert not ds.in_same(0, 3), "0 和 3 不应该在同一个集合"
    assert not ds.in_same(1, 4), "1 和 4 不应该在同一个集合"

    # 合并两个集合
    ds.join(2, 3)

    # 现在所有元素都应该在同一集合
    for i in range(5):
        for j in range(5):
            assert ds.in_same(i, j), f"{i} 和 {j} 现在应该在同一个集合"


def test_path_compression():
    """测试路径压缩"""
    ds = DisjointSet(10)

    # 创建链式结构: 0->1->2->3->4
    ds.join(0, 1)
    ds.join(1, 2)
    ds.join(2, 3)
    ds.join(3, 4)

    # 查找应该触发路径压缩
    root = ds.find_set(4)

    # 所有节点的父节点都应该是根节点
    for i in range(5):
        assert ds.find_set(i) == root, f"元素 {i} 的父节点应该是根节点 {root}"


def test_rank():
    """测试按秩合并"""
    ds = DisjointSet(10)

    # 合并两个单元素集合
    ds.join(0, 1)
    # 此时 0 或 1 的 rank 应该为 1

    # 合并另一个单元素集合
    ds.join(2, 3)

    # 合并两个高度为1的集合
    ds.join(0, 2)
    # 此时根节点的 rank 应该为 2

    # 验证 find_set 正常工作
    root1 = ds.find_set(0)
    root2 = ds.find_set(3)
    assert root1 == root2, "0 和 3 应该有相同的根"


def test_self_join():
    """测试自合并（应该没有效果）"""
    ds = DisjointSet(5)

    # 自合并不应该改变任何东西
    ds.join(0, 0)

    # 元素应该还是独立的
    assert ds.find_set(0) == 0, "自合并后根应该还是自己"
    assert not ds.in_same(0, 1), "0 和 1 不应该在同一集合"


def test_large_set():
    """测试大集合"""
    n = 1000
    ds = DisjointSet(n)

    # 合并所有偶数
    for i in range(2, n, 2):
        ds.join(0, i)

    # 合并所有奇数
    for i in range(3, n, 2):
        ds.join(1, i)

    # 验证偶数都在同一集合
    for i in range(0, n, 2):
        assert ds.in_same(0, i), f"偶数 {i} 应该和 0 在同一集合"

    # 验证奇数都在同一集合
    for i in range(1, n, 2):
        assert ds.in_same(1, i), f"奇数 {i} 应该和 1 在同一集合"

    # 验证偶数和奇数不在同一集合
    assert not ds.in_same(0, 1), "偶数和奇数不应该在同一集合"

    # 合并两个大集合
    ds.join(0, 1)

    # 现在所有元素都应该在同一集合
    for i in range(n):
        for j in range(n):
            assert ds.in_same(i, j), f"{i} 和 {j} 现在应该在同一个集合"
