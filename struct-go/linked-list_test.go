package container

import (
	"fmt"
	"testing"
)

func Test_LinkedList(t *testing.T) {
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
