package container

import (
	"container/heap"
	"fmt"
	"testing"
)

func Test_Heap(t *testing.T) {
	// Some items and their priorities.
	items := map[string]int{"banana": 3, "apple": 2, "pear": 4}

	pq := PriorityQueue{}
	i := 0
	for value, priority := range items {
		pq = append(pq, &Item{value: value, priority: priority})
		i++
	}
	heap.Init(&pq) // Establish the heap invariants

	// Insert a new item and then modify its priority.
	item := &Item{value: "orange", priority: 1}
	heap.Push(&pq, item)

	// Take the items out; they arrive in decreasing priority order.
	for pq.Len() > 0 {
		item := heap.Pop(&pq).(*Item)
		fmt.Printf("%.2d:%s \n", item.priority, item.value)
	}
}
