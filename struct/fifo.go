/**
* FIFO Queue
*
* Note:
*  require Go 1.18+
*/

package main

import (
	"fmt"
)

type FifoQueue[T any] struct {
	items []T
}

func NewFifoQueue[T any]() *FifoQueue[T] {
	return &FifoQueue[T]{
		items: make([]T, 0),
	}
}

func (d *FifoQueue[T]) PopFront() T {
	var zero T
	if d.IsEmpty() {
		return zero
	}
	item := d.items[0]
	// 注意：这涉及到元素移动和内存重新分配，效率相对较低（O(n)）
	d.items = d.items[1:]
	return item
}

func (d *FifoQueue[T]) PeekFront() T {
	var zero T
	if d.IsEmpty() {
		return zero
	}
	return d.items[0]
}

func (d *FifoQueue[T]) PushBack(item T) {
	d.items = append(d.items, item)
}

func (d *FifoQueue[T]) IsEmpty() bool {
	return len(d.items) == 0
}

func (d *FifoQueue[T]) Size() int {
	return len(d.items)
}

func main() {
	queue := NewFifoQueue[int]()

	queue.PushBack(10)
	queue.PushBack(20)
	fmt.Printf("PushBack: %v, Size: %d\n", queue.items, queue.Size()) // Output: [10 20], Size: 2

	fmt.Printf("PeekFront: %v\n", queue.PeekFront()) // Output: 10

	frontItem := queue.PopFront()
	fmt.Printf("PopFront: %v, Current: %v\n", frontItem, queue.items) // Output: 10, Current: [20]

	fmt.Printf("Final Size: %d, IsEmpty: %t\n", queue.Size(), queue.IsEmpty()) // Output: Final Size: 1, IsEmpty: false
}