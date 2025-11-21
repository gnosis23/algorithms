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

	list.ForEach(func(index int, value int) {
		fmt.Println(value)
	})

	list2 := InitLinkedList[string]()
	list2.Push("linked")
	list2.Push("list")
	list2.Push("is")
	list2.Push("good")

	list2.ForEach(func(index int, value string) {
		fmt.Println(value)
	})
}
