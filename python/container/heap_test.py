#!/usr/bin/env python3
"""
堆 (Heap) 测试
"""

# 导入 heap 模块中的函数，但不执行 heap.py 的 main()
import heap


def test_heapsort_basic():
    """测试堆排序基本功能"""
    # 测试空列表
    assert heap.heapsort([]) == []

    # 测试单个元素
    assert heap.heapsort([5]) == [5]

    # 测试多个元素
    assert heap.heapsort([4, 0, 0, 8]) == [0, 0, 4, 8]

    # 测试已排序列表
    assert heap.heapsort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # 测试逆序列表
    assert heap.heapsort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # 测试重复元素
    assert heap.heapsort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [
        1,
        1,
        2,
        3,
        3,
        4,
        5,
        5,
        5,
        6,
        9,
    ]


def test_heapsort_large():
    """测试堆排序大列表"""
    import random

    # 生成随机列表
    random.seed(42)  # 固定随机种子以便重现
    large_list = [random.randint(-1000, 1000) for _ in range(1000)]

    # 使用堆排序
    sorted_by_heap = heap.heapsort(large_list)

    # 使用 Python 内置排序验证
    sorted_by_python = sorted(large_list)

    assert sorted_by_heap == sorted_by_python, "堆排序结果应该与 Python 内置排序一致"


def test_priority_queue_basic():
    """测试优先队列基本功能"""
    # 测试空任务列表
    assert heap.priority_queue([]) == []

    # 测试单个任务
    assert heap.priority_queue([(5, "task1")]) == [(5, "task1")]

    # 测试多个任务（来自原文件示例）
    tasks = [(5, "code"), (7, "release"), (1, "doc")]
    result = heap.priority_queue(tasks)
    assert result == [
        (1, "doc"),
        (5, "code"),
        (7, "release"),
    ], f"期望 [(1, 'doc'), (5, 'code'), (7, 'release')]，得到 {result}"

    # 测试相同优先级的任务
    tasks = [(3, "task3"), (1, "task1"), (3, "task2"), (2, "task4")]
    result = heap.priority_queue(tasks)
    # 注意：当优先级相同时，Python 会比较元组的第二个元素
    assert result == [(1, "task1"), (2, "task4"), (3, "task2"), (3, "task3")]


def test_priority_queue_complex():
    """测试复杂优先队列"""
    # 测试负优先级
    tasks = [(-5, "low"), (0, "medium"), (5, "high")]
    assert heap.priority_queue(tasks) == [(-5, "low"), (0, "medium"), (5, "high")]

    # 测试浮点数优先级
    tasks = [(3.14, "pi"), (2.71, "e"), (1.41, "sqrt2")]
    assert heap.priority_queue(tasks) == [(1.41, "sqrt2"), (2.71, "e"), (3.14, "pi")]

    # 测试字符串优先级（按字典序）
    tasks = [("z", "last"), ("a", "first"), ("m", "middle")]
    assert heap.priority_queue(tasks) == [
        ("a", "first"),
        ("m", "middle"),
        ("z", "last"),
    ]


def test_heap_properties():
    """测试堆属性"""
    # 验证 heapsort 使用的是小根堆
    test_list = [9, 3, 7, 1, 5]
    sorted_list = heap.heapsort(test_list)

    # 验证排序结果
    assert sorted_list == [1, 3, 5, 7, 9]

    # 验证 priority_queue 也是小根堆
    tasks = [(9, "nine"), (3, "three"), (7, "seven"), (1, "one"), (5, "five")]
    queue_result = heap.priority_queue(tasks)
    assert queue_result == [
        (1, "one"),
        (3, "three"),
        (5, "five"),
        (7, "seven"),
        (9, "nine"),
    ]


def test_edge_cases():
    """测试边界情况"""
    # 测试所有元素相同
    assert heap.heapsort([7, 7, 7, 7]) == [7, 7, 7, 7]

    # 测试包含 None（应该会报错，因为 None 不能比较）
    try:
        heap.heapsort([3, None, 1])
        print("⚠️ 包含 None 的列表没有报错，这可能不是预期行为")
    except TypeError:
        pass  # 预期行为

    # 测试混合类型（应该会报错）
    try:
        heap.heapsort([3, "string", 1])
        print("⚠️ 混合类型的列表没有报错，这可能不是预期行为")
    except TypeError:
        pass  # 预期行为

    # 测试非常大的数字
    large_numbers = [10**100, -(10**100), 0, 10**50, -(10**50)]
    assert heap.heapsort(large_numbers) == [-(10**100), -(10**50), 0, 10**50, 10**100]
