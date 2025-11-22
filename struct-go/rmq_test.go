package container

import (
	"math"
	"testing"
)

// TestRangeMinQuery_Init 测试初始化功能
func TestRangeMinQuery_Init(t *testing.T) {
	// 测试不同大小的初始化
	testCases := []struct {
		n        int
		expected int
	}{
		{1, 1},   // 最小容量
		{2, 2},   // 刚好是2的幂
		{3, 4},   // 需要向上取整到2的幂
		{5, 8},   // 需要向上取整到2的幂
		{8, 8},   // 刚好是2的幂
		{15, 16}, // 需要向上取整到2的幂
	}

	for _, tc := range testCases {
		rmq := InitRangeMinQuery(tc.n)
		if rmq.cap != tc.expected {
			t.Errorf("InitRangeMinQuery(%d): expected capacity %d, got %d", tc.n, tc.expected, rmq.cap)
		}
		if len(rmq.data) != 2*tc.expected-1 {
			t.Errorf("InitRangeMinQuery(%d): expected data length %d, got %d", tc.n, 2*tc.expected-1, len(rmq.data))
		}
	}
}

// TestRangeMinQuery_UpdateAndQuery 测试更新和查询功能
func TestRangeMinQuery_UpdateAndQuery(t *testing.T) {
	rmq := InitRangeMinQuery(8)

	// 初始化数据
	values := []int{3, 1, 4, 1, 5, 9, 2, 6}
	for i, v := range values {
		rmq.Update(i, v)
	}

	// 测试各种查询范围
	testCases := []struct {
		a        int
		b        int
		expected int
	}{
		// 单点查询
		{0, 1, 3}, // [0,1) = 3
		{1, 2, 1}, // [1,2) = 1
		{2, 3, 4}, // [2,3) = 4
		{3, 4, 1}, // [3,4) = 1
		{4, 5, 5}, // [4,5) = 5
		{5, 6, 9}, // [5,6) = 9
		{6, 7, 2}, // [6,7) = 2
		{7, 8, 6}, // [7,8) = 6

		// 区间查询
		{0, 2, 1}, // [0,2) = min(3,1) = 1
		{1, 4, 1}, // [1,4) = min(1,4,1) = 1
		{2, 6, 1}, // [2,6) = min(4,1,5,9) = 1
		{0, 8, 1}, // [0,8) = min(3,1,4,1,5,9,2,6) = 1
		{4, 8, 2}, // [4,8) = min(5,9,2,6) = 2
		{0, 4, 1}, // [0,4) = min(3,1,4,1) = 1
		{5, 7, 2}, // [5,7) = min(9,2) = 2
		{6, 8, 2}, // [6,8) = min(2,6) = 2
	}

	for _, tc := range testCases {
		result := rmq.QueryAll(tc.a, tc.b)
		if result != tc.expected {
			t.Errorf("Query(%d, %d): expected %d, got %d", tc.a, tc.b, tc.expected, result)
		}
	}
}

// TestRangeMinQuery_UpdateChanges 测试更新操作改变最小值
func TestRangeMinQuery_UpdateChanges(t *testing.T) {
	rmq := InitRangeMinQuery(4)

	// 初始数据
	rmq.Update(0, 5)
	rmq.Update(1, 3)
	rmq.Update(2, 7)
	rmq.Update(3, 2)

	// 初始查询
	if result := rmq.QueryAll(0, 4); result != 2 {
		t.Errorf("Initial query [0,4): expected 2, got %d", result)
	}

	// 更新最小值位置
	rmq.Update(3, 10)
	if result := rmq.QueryAll(0, 4); result != 3 {
		t.Errorf("After updating position 3: expected 3, got %d", result)
	}

	// 更新新的最小值
	rmq.Update(0, 1)
	if result := rmq.QueryAll(0, 4); result != 1 {
		t.Errorf("After updating position 0: expected 1, got %d", result)
	}

	// 更新中间位置
	rmq.Update(2, 0)
	if result := rmq.QueryAll(0, 4); result != 0 {
		t.Errorf("After updating position 2: expected 0, got %d", result)
	}
}

// TestRangeMinQuery_EdgeCases 测试边界情况
func TestRangeMinQuery_EdgeCases(t *testing.T) {
	rmq := InitRangeMinQuery(1)

	// 单元素数组
	rmq.Update(0, 42)
	if result := rmq.QueryAll(0, 1); result != 42 {
		t.Errorf("Single element query: expected 42, got %d", result)
	}

	// 空区间查询
	if result := rmq.QueryAll(1, 1); result != math.MaxInt {
		t.Errorf("Empty range query: expected math.MaxInt, got %d", result)
	}

	// 超出范围的查询
	if result := rmq.QueryAll(0, 2); result != 42 {
		t.Errorf("Query beyond capacity: expected 42, got %d", result)
	}
}

// TestRangeMinQuery_NegativeNumbers 测试负数
func TestRangeMinQuery_NegativeNumbers(t *testing.T) {
	rmq := InitRangeMinQuery(4)

	values := []int{-3, -1, -5, -2}
	for i, v := range values {
		rmq.Update(i, v)
	}

	testCases := []struct {
		a        int
		b        int
		expected int
	}{
		{0, 1, -3},
		{1, 2, -1},
		{2, 3, -5},
		{3, 4, -2},
		{0, 2, -3}, // min(-3, -1) = -3
		{1, 4, -5}, // min(-1, -5, -2) = -5
		{0, 4, -5}, // min(-3, -1, -5, -2) = -5
	}

	for _, tc := range testCases {
		result := rmq.QueryAll(tc.a, tc.b)
		if result != tc.expected {
			t.Errorf("Query(%d, %d) with negative numbers: expected %d, got %d", tc.a, tc.b, tc.expected, result)
		}
	}
}

// TestRangeMinQuery_LargeNumbers 测试大数
func TestRangeMinQuery_LargeNumbers(t *testing.T) {
	rmq := InitRangeMinQuery(3)

	largeValues := []int{math.MaxInt - 1, math.MaxInt, math.MaxInt - 2}
	for i, v := range largeValues {
		rmq.Update(i, v)
	}

	if result := rmq.QueryAll(0, 3); result != math.MaxInt-2 {
		t.Errorf("Large numbers query: expected %d, got %d", math.MaxInt-2, result)
	}
}

// TestRangeMinQuery_SequentialUpdates 测试连续更新
func TestRangeMinQuery_SequentialUpdates(t *testing.T) {
	rmq := InitRangeMinQuery(3)

	// 初始值
	rmq.Update(0, 10)
	rmq.Update(1, 20)
	rmq.Update(2, 30)

	// 验证初始状态
	if result := rmq.QueryAll(0, 3); result != 10 {
		t.Errorf("Initial state: expected 10, got %d", result)
	}

	// 连续更新
	rmq.Update(1, 5) // 现在数组: [10, 5, 30]
	if result := rmq.QueryAll(0, 3); result != 5 {
		t.Errorf("After first update: expected 5, got %d", result)
	}

	rmq.Update(0, 8) // 现在数组: [8, 5, 30]
	if result := rmq.QueryAll(0, 3); result != 5 {
		t.Errorf("After second update: expected 5, got %d", result)
	}

	rmq.Update(2, 3) // 现在数组: [8, 5, 3]
	if result := rmq.QueryAll(0, 3); result != 3 {
		t.Errorf("After third update: expected 3, got %d", result)
	}
}
