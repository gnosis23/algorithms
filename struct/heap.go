package main

import (
	"container/heap"
	"fmt"
)

type Item struct {
	value    string
	priority int
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	// Less first
	return pq[i].priority < pq[j].priority
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
}

func (pq *PriorityQueue) Push(x any) {
	item := x.(*Item)
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() any {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil // avoid memory leak
	*pq = old[0 : n-1]
	return item
}

func main() {
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
