package container

import (
	"container/heap"
	"testing"
)

func TestPriorityQueue_Len(t *testing.T) {
	pq := PriorityQueue{}
	if pq.Len() != 0 {
		t.Errorf("Expected length 0, got %d", pq.Len())
	}

	pq = append(pq, &Item{value: "test", priority: 1})
	if pq.Len() != 1 {
		t.Errorf("Expected length 1, got %d", pq.Len())
	}
}

func TestPriorityQueue_Less(t *testing.T) {
	pq := PriorityQueue{
		&Item{value: "low", priority: 1},
		&Item{value: "high", priority: 5},
	}

	if !pq.Less(0, 1) {
		t.Error("Expected item at index 0 to be less than item at index 1")
	}

	if pq.Less(1, 0) {
		t.Error("Expected item at index 1 to not be less than item at index 0")
	}
}

func TestPriorityQueue_Swap(t *testing.T) {
	pq := PriorityQueue{
		&Item{value: "first", priority: 1},
		&Item{value: "second", priority: 2},
	}

	pq.Swap(0, 1)

	if pq[0].value != "second" || pq[0].priority != 2 {
		t.Error("Swap failed for index 0")
	}
	if pq[1].value != "first" || pq[1].priority != 1 {
		t.Error("Swap failed for index 1")
	}
}

func TestPriorityQueue_Push(t *testing.T) {
	pq := &PriorityQueue{}
	item := &Item{value: "test", priority: 1}

	pq.Push(item)

	if pq.Len() != 1 {
		t.Errorf("Expected length 1 after push, got %d", pq.Len())
	}
	if (*pq)[0] != item {
		t.Error("Pushed item not found at expected position")
	}
}

func TestPriorityQueue_Pop(t *testing.T) {
	pq := &PriorityQueue{
		&Item{value: "first", priority: 1},
		&Item{value: "second", priority: 2},
	}

	item := pq.Pop().(*Item)

	if item.value != "second" || item.priority != 2 {
		t.Error("Pop did not return the last item")
	}
	if pq.Len() != 1 {
		t.Errorf("Expected length 1 after pop, got %d", pq.Len())
	}
}

func TestPriorityQueue_HeapOperations(t *testing.T) {
	pq := &PriorityQueue{}
	heap.Init(pq)

	// Test pushing multiple items
	items := []*Item{
		{value: "banana", priority: 3},
		{value: "apple", priority: 2},
		{value: "pear", priority: 4},
	}

	for _, item := range items {
		heap.Push(pq, item)
	}

	if pq.Len() != 3 {
		t.Errorf("Expected length 3 after pushing items, got %d", pq.Len())
	}

	// Test popping items in priority order
	expectedOrder := []string{"apple", "banana", "pear"}
	for i, expected := range expectedOrder {
		item := heap.Pop(pq).(*Item)
		if item.value != expected {
			t.Errorf("Expected %s at position %d, got %s", expected, i, item.value)
		}
	}

	if pq.Len() != 0 {
		t.Errorf("Expected empty queue after popping all items, got length %d", pq.Len())
	}
}

func TestPriorityQueue_EmptyPop(t *testing.T) {
	pq := &PriorityQueue{}
	heap.Init(pq)

	// The Go heap implementation panics when popping from empty heap
	// This is expected behavior, so we test that it actually panics
	func() {
		defer func() {
			if r := recover(); r == nil {
				t.Error("Expected panic when popping from empty heap")
			}
		}()
		pq.Pop()
	}()
}

func TestPriorityQueue_UpdatePriority(t *testing.T) {
	pq := &PriorityQueue{}
	heap.Init(pq)

	// Add items
	item1 := &Item{value: "low", priority: 1}
	item2 := &Item{value: "medium", priority: 3}
	item3 := &Item{value: "high", priority: 5}

	heap.Push(pq, item1)
	heap.Push(pq, item2)
	heap.Push(pq, item3)

	// Update priority of item2 to be the highest
	item2.priority = 0
	heap.Fix(pq, 1) // Fix the heap after priority change

	// Now item2 should be at the top
	top := heap.Pop(pq).(*Item)
	if top != item2 {
		t.Error("Expected item2 to be at the top after priority update")
	}
}

func TestPriorityQueue_MixedOperations(t *testing.T) {
	pq := &PriorityQueue{}
	heap.Init(pq)

	// Test mixed push and pop operations
	heap.Push(pq, &Item{value: "a", priority: 5})
	heap.Push(pq, &Item{value: "b", priority: 1})
	heap.Push(pq, &Item{value: "c", priority: 3})

	// Pop the smallest
	item := heap.Pop(pq).(*Item)
	if item.value != "b" {
		t.Errorf("Expected 'b', got '%s'", item.value)
	}

	// Push more items
	heap.Push(pq, &Item{value: "d", priority: 2})
	heap.Push(pq, &Item{value: "e", priority: 0})

	// Pop in correct order
	expectedOrder := []string{"e", "d", "c", "a"}
	for _, expected := range expectedOrder {
		item := heap.Pop(pq).(*Item)
		if item.value != expected {
			t.Errorf("Expected '%s', got '%s'", expected, item.value)
		}
	}
}