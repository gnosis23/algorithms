package container

type LinkedList[T any] struct {
	Head *ListItem[T]
	Tail *ListItem[T]
}

type ListItem[T any] struct {
	Value T
	Next  *ListItem[T]
}

func InitLinkedList[T any]() *LinkedList[T] {
	return &LinkedList[T]{}
}

func (l *LinkedList[T]) Push(x T) {
	if l.Head == nil {
		l.Head = &ListItem[T]{Value: x}
		l.Tail = l.Head
	} else {
		l.Tail.Next = &ListItem[T]{Value: x}
		l.Tail = l.Tail.Next
	}
}
