package container

// node represents a single node in the linked list
type node[T any] struct {
	value T
	next  *node[T]
}

type FifoQueue[T any] struct {
	head *node[T]
	tail *node[T]
	size int
}

func InitFifoQueue[T any]() *FifoQueue[T] {
	return &FifoQueue[T]{
		head: nil,
		tail: nil,
		size: 0,
	}
}

func (q *FifoQueue[T]) PopFront() T {
	var zero T
	if q.IsEmpty() {
		return zero
	}

	item := q.head.value
	q.head = q.head.next
	q.size--

	// If the queue becomes empty after popping, update tail to nil
	if q.head == nil {
		q.tail = nil
	}

	return item
}

func (q *FifoQueue[T]) PeekFront() T {
	var zero T
	if q.IsEmpty() {
		return zero
	}
	return q.head.value
}

func (q *FifoQueue[T]) PushBack(item T) {
	newNode := &node[T]{
		value: item,
		next:  nil,
	}

	if q.IsEmpty() {
		q.head = newNode
		q.tail = newNode
	} else {
		q.tail.next = newNode
		q.tail = newNode
	}
	q.size++
}

func (q *FifoQueue[T]) IsEmpty() bool {
	return q.size == 0
}

func (q *FifoQueue[T]) Size() int {
	return q.size
}
