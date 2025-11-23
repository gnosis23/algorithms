package container

type LinkedList[T any] struct {
	head *ListItem[T]
	tail *ListItem[T]
}

type ListItem[T any] struct {
	Value T
	Next  *ListItem[T]
}

func InitLinkedList[T any]() *LinkedList[T] {
	return &LinkedList[T]{}
}

func (l *LinkedList[T]) Push(x T) {
	if l.head == nil {
		l.head = &ListItem[T]{Value: x}
		l.tail = l.head
	} else {
		l.tail.Next = &ListItem[T]{Value: x}
		l.tail = l.tail.Next
	}
}

func (l *LinkedList[T]) ForEach(callback func(index int, value T)) {
	current := l.head
	index := 0
	for current != nil {
		callback(index, current.Value)
		current = current.Next
		index++
	}
}
