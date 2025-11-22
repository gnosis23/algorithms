package container

import (
	"testing"
)

func Test_BinaryIndexedTree_Init(t *testing.T) {
	// Test initialization with different sizes
	tests := []struct {
		size int
	}{
		{1},
		{5},
		{10},
		{100},
	}

	for _, tt := range tests {
		bit := InitBinaryIndexedTree(tt.size)
		if bit == nil {
			t.Errorf("InitBinaryIndexedTree(%d) returned nil", tt.size)
			break
		}
		if bit.n != tt.size {
			t.Errorf("Expected n=%d, got %d", tt.size, bit.n)
		}
		if len(bit.data) != tt.size+1 {
			t.Errorf("Expected data length %d, got %d", tt.size+1, len(bit.data))
		}
	}
}

func Test_BinaryIndexedTree_Sum_Empty(t *testing.T) {
	// Test Sum on empty tree
	bit := InitBinaryIndexedTree(5)

	// Sum of first 0 elements should be 0
	if result := bit.Sum(0); result != 0 {
		t.Errorf("Expected Sum(0)=0, got %d", result)
	}

	// Sum of first 1 element should be 0 (no additions yet)
	if result := bit.Sum(1); result != 0 {
		t.Errorf("Expected Sum(1)=0, got %d", result)
	}

	// Sum of first 3 elements should be 0
	if result := bit.Sum(3); result != 0 {
		t.Errorf("Expected Sum(3)=0, got %d", result)
	}
}

func Test_BinaryIndexedTree_AddAndSum_Basic(t *testing.T) {
	bit := InitBinaryIndexedTree(5)

	// Add to position 0 (which becomes index 1 in BIT)
	bit.Add(0, 10)

	// Verify sums
	if result := bit.Sum(1); result != 10 {
		t.Errorf("Expected Sum(1)=10 after Add(0,10), got %d", result)
	}
	if result := bit.Sum(2); result != 10 {
		t.Errorf("Expected Sum(2)=10 after Add(0,10), got %d", result)
	}
	if result := bit.Sum(5); result != 10 {
		t.Errorf("Expected Sum(5)=10 after Add(0,10), got %d", result)
	}
}

func Test_BinaryIndexedTree_AddAndSum_Multiple(t *testing.T) {
	bit := InitBinaryIndexedTree(5)

	// Add multiple values
	bit.Add(0, 5) // Position 0: 5
	bit.Add(1, 3) // Position 1: 3
	bit.Add(2, 7) // Position 2: 7
	bit.Add(3, 2) // Position 3: 2
	bit.Add(4, 8) // Position 4: 8

	// Test cumulative sums
	testCases := []struct {
		index    int
		expected int
	}{
		{1, 5},  // Sum of first 1 element: 5
		{2, 8},  // Sum of first 2 elements: 5 + 3 = 8
		{3, 15}, // Sum of first 3 elements: 5 + 3 + 7 = 15
		{4, 17}, // Sum of first 4 elements: 5 + 3 + 7 + 2 = 17
		{5, 25}, // Sum of first 5 elements: 5 + 3 + 7 + 2 + 8 = 25
	}

	for _, tc := range testCases {
		if result := bit.Sum(tc.index); result != tc.expected {
			t.Errorf("Expected Sum(%d)=%d, got %d", tc.index, tc.expected, result)
		}
	}
}

func Test_BinaryIndexedTree_AddAndSum_WithUpdates(t *testing.T) {
	bit := InitBinaryIndexedTree(5)

	// Initial additions
	bit.Add(0, 5)
	bit.Add(1, 3)
	bit.Add(2, 7)

	// Verify initial sums
	if result := bit.Sum(3); result != 15 {
		t.Errorf("Expected initial Sum(3)=15, got %d", result)
	}

	// Update existing positions
	bit.Add(1, 2)  // Add 2 to position 1 (3 + 2 = 5)
	bit.Add(0, -1) // Subtract 1 from position 0 (5 - 1 = 4)

	// Verify updated sums
	if result := bit.Sum(1); result != 4 {
		t.Errorf("Expected updated Sum(1)=4, got %d", result)
	}
	if result := bit.Sum(2); result != 9 {
		t.Errorf("Expected updated Sum(2)=9, got %d", result)
	}
	if result := bit.Sum(3); result != 16 {
		t.Errorf("Expected updated Sum(3)=16, got %d", result)
	}
}

func Test_BinaryIndexedTree_EdgeCases(t *testing.T) {
	// Test with size 1
	bit := InitBinaryIndexedTree(1)
	bit.Add(0, 10)
	if result := bit.Sum(1); result != 10 {
		t.Errorf("Expected Sum(1)=10 for size=1, got %d", result)
	}

	// Test with size 0 (should handle gracefully)
	bit0 := InitBinaryIndexedTree(0)
	if bit0.n != 0 {
		t.Errorf("Expected n=0 for size=0, got %d", bit0.n)
	}
	if len(bit0.data) != 1 {
		t.Errorf("Expected data length=1 for size=0, got %d", len(bit0.data))
	}

	// Sum should work for size 0
	if result := bit0.Sum(0); result != 0 {
		t.Errorf("Expected Sum(0)=0 for size=0, got %d", result)
	}
}
