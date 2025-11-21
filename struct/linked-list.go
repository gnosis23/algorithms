package main

import "fmt"

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

func main() {
	list := InitLinkedList[int]()
	list.Push(1)
	list.Push(2)
	list.Push(3)

	ptr := list.Head
	for ptr != nil {
		fmt.Println(ptr.Value)
		ptr = ptr.Next
	}

	list2 := InitLinkedList[string]()
	list2.Push("linked")
	list2.Push("list")
	list2.Push("is")
	list2.Push("good")

	ptr2 := list2.Head
	for ptr2 != nil {
		fmt.Println(ptr2.Value)
		ptr2 = ptr2.Next
	}
}
