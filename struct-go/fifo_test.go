package container

import (
	"testing"
)

func Test_Fifo(t *testing.T) {
	queue := InitFifoQueue[int]()

	// Test initial state
	if !queue.IsEmpty() {
		t.Error("New queue should be empty")
	}
	if queue.Size() != 0 {
		t.Errorf("Expected size 0, got %d", queue.Size())
	}

	// Test PushBack
	queue.PushBack(10)
	queue.PushBack(20)
	queue.PushBack(30)

	if queue.Size() != 3 {
		t.Errorf("Expected size 3 after pushing 3 items, got %d", queue.Size())
	}
	if queue.IsEmpty() {
		t.Error("Queue should not be empty after pushing items")
	}

	// Test PeekFront
	front := queue.PeekFront()
	if front != 10 {
		t.Errorf("Expected PeekFront to return 10, got %d", front)
	}

	// Test PopFront
	popped := queue.PopFront()
	if popped != 10 {
		t.Errorf("Expected PopFront to return 10, got %d", popped)
	}
	if queue.Size() != 2 {
		t.Errorf("Expected size 2 after popping one item, got %d", queue.Size())
	}

	// Test multiple pops
	front = queue.PeekFront()
	if front != 20 {
		t.Errorf("Expected PeekFront to return 20, got %d", front)
	}

	popped = queue.PopFront()
	if popped != 20 {
		t.Errorf("Expected PopFront to return 20, got %d", popped)
	}

	popped = queue.PopFront()
	if popped != 30 {
		t.Errorf("Expected PopFront to return 30, got %d", popped)
	}

	// Test empty queue behavior
	if !queue.IsEmpty() {
		t.Error("Queue should be empty after popping all items")
	}
	if queue.Size() != 0 {
		t.Errorf("Expected size 0, got %d", queue.Size())
	}

	// Test PopFront on empty queue
	zeroValue := queue.PopFront()
	if zeroValue != 0 {
		t.Errorf("Expected zero value from PopFront on empty queue, got %d", zeroValue)
	}

	// Test PeekFront on empty queue
	zeroValue = queue.PeekFront()
	if zeroValue != 0 {
		t.Errorf("Expected zero value from PeekFront on empty queue, got %d", zeroValue)
	}
}

func Test_Fifo_String(t *testing.T) {
	queue := InitFifoQueue[string]()

	queue.PushBack("hello")
	queue.PushBack("world")

	if queue.Size() != 2 {
		t.Errorf("Expected size 2, got %d", queue.Size())
	}

	front := queue.PeekFront()
	if front != "hello" {
		t.Errorf("Expected 'hello', got '%s'", front)
	}

	popped := queue.PopFront()
	if popped != "hello" {
		t.Errorf("Expected 'hello', got '%s'", popped)
	}

	popped = queue.PopFront()
	if popped != "world" {
		t.Errorf("Expected 'world', got '%s'", popped)
	}

	// Test empty string queue
	zeroValue := queue.PopFront()
	if zeroValue != "" {
		t.Errorf("Expected empty string from PopFront on empty queue, got '%s'", zeroValue)
	}
}
