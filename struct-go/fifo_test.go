package container

import (
	"fmt"
	"testing"
)

func Test_Fifo(t *testing.T) {
	queue := NewFifoQueue[int]()

	queue.PushBack(10)
	queue.PushBack(20)
	fmt.Printf("PushBack: %v, Size: %d\n", queue.items, queue.Size()) // Output: [10 20], Size: 2

	fmt.Printf("PeekFront: %v\n", queue.PeekFront()) // Output: 10

	frontItem := queue.PopFront()
	fmt.Printf("PopFront: %v, Current: %v\n", frontItem, queue.items) // Output: 10, Current: [20]

	fmt.Printf("Final Size: %d, IsEmpty: %t\n", queue.Size(), queue.IsEmpty()) // Output: Final Size: 1, IsEmpty: false
	if queue.Size() != 1 {
		t.Errorf("Expect queue size = %d", 1)
	}
}
