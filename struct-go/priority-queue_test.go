package container

import (
	"testing"
)

func TestPriorityQueue_New(t *testing.T) {
	pq := InitPriorityQueue()
	if pq.Len() != 0 {
		t.Errorf("Expected length 0, got %d", pq.Len())
	}
	if !pq.IsEmpty() {
		t.Error("Expected empty queue")
	}
}

func TestPriorityQueue_Push(t *testing.T) {
	pq := InitPriorityQueue()
	pq.Push("test", 1)

	if pq.Len() != 1 {
		t.Errorf("Expected length 1 after push, got %d", pq.Len())
	}
	if pq.IsEmpty() {
		t.Error("Expected non-empty queue after push")
	}
}

func TestPriorityQueue_Pop(t *testing.T) {
	pq := InitPriorityQueue()
	pq.Push("first", 1)
	pq.Push("second", 2)

	item := pq.Pop()
	if item == nil {
		t.Fatal("Expected non-nil item from Pop")
	}
	if item.Value != "first" || item.Priority != 1 {
		t.Errorf("Expected item with value 'first' and priority 1, got %+v", item)
	}
	if pq.Len() != 1 {
		t.Errorf("Expected length 1 after pop, got %d", pq.Len())
	}

	item = pq.Pop()
	if item == nil {
		t.Fatal("Expected non-nil item from Pop")
	}
	if item.Value != "second" || item.Priority != 2 {
		t.Errorf("Expected item with value 'second' and priority 2, got %+v", item)
	}
	if pq.Len() != 0 {
		t.Errorf("Expected length 0 after popping all items, got %d", pq.Len())
	}
}

func TestPriorityQueue_Peek(t *testing.T) {
	pq := InitPriorityQueue()

	// Test peek on empty queue
	if pq.Peek() != nil {
		t.Error("Expected nil when peeking empty queue")
	}

	pq.Push("test", 1)
	item := pq.Peek()
	if item == nil {
		t.Fatal("Expected non-nil item from Peek")
	}
	if item.Value != "test" || item.Priority != 1 {
		t.Errorf("Expected item with value 'test' and priority 1, got %+v", item)
	}
	if pq.Len() != 1 {
		t.Errorf("Expected length unchanged after peek, got %d", pq.Len())
	}
}

func TestPriorityQueue_HeapOperations(t *testing.T) {
	pq := InitPriorityQueue()

	// Test pushing multiple items
	pq.Push("banana", 3)
	pq.Push("apple", 2)
	pq.Push("pear", 4)

	if pq.Len() != 3 {
		t.Errorf("Expected length 3 after pushing items, got %d", pq.Len())
	}

	// Test popping items in priority order
	expectedOrder := []string{"apple", "banana", "pear"}
	for i, expected := range expectedOrder {
		item := pq.Pop()
		if item == nil {
			t.Fatalf("Expected non-nil item at position %d", i)
		}
		if item.Value != expected {
			t.Errorf("Expected %s at position %d, got %s", expected, i, item.Value)
		}
	}

	if pq.Len() != 0 {
		t.Errorf("Expected empty queue after popping all items, got length %d", pq.Len())
	}
}

func TestPriorityQueue_EmptyPop(t *testing.T) {
	pq := InitPriorityQueue()

	// Our implementation returns nil when popping from empty queue
	item := pq.Pop()
	if item != nil {
		t.Error("Expected nil when popping from empty queue")
	}
}

func TestPriorityQueue_UpdatePriority(t *testing.T) {
	pq := InitPriorityQueue()

	// Add items
	pq.Push("low", 1)
	pq.Push("medium", 3)
	pq.Push("high", 5)

	// Update priority of "medium" to be the highest
	if !pq.Update("medium", 0) {
		t.Error("Failed to update priority")
	}

	// Now "medium" should be at the top
	top := pq.Pop()
	if top.Value != "medium" {
		t.Errorf("Expected 'medium' to be at the top after priority update, got %s", top.Value)
	}
}

func TestPriorityQueue_UpdateNonExistent(t *testing.T) {
	pq := InitPriorityQueue()
	pq.Push("test", 1)

	// Try to update non-existent item
	if pq.Update("nonexistent", 0) {
		t.Error("Expected false when updating non-existent item")
	}
}

func TestPriorityQueue_Remove(t *testing.T) {
	pq := InitPriorityQueue()
	pq.Push("a", 1)
	pq.Push("b", 2)
	pq.Push("c", 3)

	// Remove middle item
	if !pq.Remove("b") {
		t.Error("Failed to remove item")
	}
	if pq.Len() != 2 {
		t.Errorf("Expected length 2 after removal, got %d", pq.Len())
	}

	// Verify remaining items
	item1 := pq.Pop()
	item2 := pq.Pop()
	if item1.Value != "a" || item2.Value != "c" {
		t.Errorf("Expected items 'a' and 'c' after removal, got %s and %s", item1.Value, item2.Value)
	}
}

func TestPriorityQueue_RemoveNonExistent(t *testing.T) {
	pq := InitPriorityQueue()
	pq.Push("test", 1)

	// Try to remove non-existent item
	if pq.Remove("nonexistent") {
		t.Error("Expected false when removing non-existent item")
	}
}

func TestPriorityQueue_MixedOperations(t *testing.T) {
	pq := InitPriorityQueue()

	// Test mixed push and pop operations
	pq.Push("a", 5)
	pq.Push("b", 1)
	pq.Push("c", 3)

	// Pop the smallest
	item := pq.Pop()
	if item.Value != "b" {
		t.Errorf("Expected 'b', got '%s'", item.Value)
	}

	// Push more items
	pq.Push("d", 2)
	pq.Push("e", 0)

	// Pop in correct order
	expectedOrder := []string{"e", "d", "c", "a"}
	for _, expected := range expectedOrder {
		item := pq.Pop()
		if item.Value != expected {
			t.Errorf("Expected '%s', got '%s'", expected, item.Value)
		}
	}
}

func TestPriorityQueue_ComplexScenario(t *testing.T) {
	pq := InitPriorityQueue()

	// Add items with same priority
	pq.Push("a", 1)
	pq.Push("b", 1)
	pq.Push("c", 1)

	// With heap implementation, same priority items may not maintain insertion order
	// Just verify we get all three items and they all have priority 1
	items := make([]*PriorityQueueItem, 3)
	for i := 0; i < 3; i++ {
		items[i] = pq.Pop()
		if items[i] == nil {
			t.Fatalf("Expected non-nil item at position %d", i)
		}
		if items[i].Priority != 1 {
			t.Errorf("Expected priority 1, got %d", items[i].Priority)
		}
	}

	// Verify we got all three distinct values
	values := make(map[string]bool)
	for _, item := range items {
		values[item.Value] = true
	}
	if len(values) != 3 {
		t.Errorf("Expected 3 distinct values, got %v", values)
	}
}

func TestPriorityQueue_UpdateAndRemove(t *testing.T) {
	pq := InitPriorityQueue()
	pq.Push("item1", 5)
	pq.Push("item2", 3)
	pq.Push("item3", 7)

	// Update item2 to have higher priority
	pq.Update("item2", 1)

	// Remove item3
	pq.Remove("item3")

	// Should get item2 first, then item1
	item1 := pq.Pop()
	item2 := pq.Pop()

	if item1.Value != "item2" || item1.Priority != 1 {
		t.Errorf("Expected item2 with priority 1 first, got %+v", item1)
	}
	if item2.Value != "item1" || item2.Priority != 5 {
		t.Errorf("Expected item1 with priority 5 second, got %+v", item2)
	}
}
