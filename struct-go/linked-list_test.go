package container

import (
	"testing"
)

func TestInitLinkedList(t *testing.T) {
	list := InitLinkedList[int]()

	if list.head != nil {
		t.Error("New linked list should have nil head")
	}
	if list.tail != nil {
		t.Error("New linked list should have nil tail")
	}
}

func TestLinkedList_Push(t *testing.T) {
	list := InitLinkedList[int]()

	// Test pushing first element
	list.Push(42)
	if list.head == nil || list.tail == nil {
		t.Error("Head and tail should not be nil after pushing first element")
	}
	if list.head.Value != 42 {
		t.Errorf("Expected head value 42, got %d", list.head.Value)
	}
	if list.tail.Value != 42 {
		t.Errorf("Expected tail value 42, got %d", list.tail.Value)
	}
	if list.head != list.tail {
		t.Error("Head and tail should be the same for single element list")
	}

	// Test pushing second element
	list.Push(100)
	if list.head.Value != 42 {
		t.Errorf("Head value should remain 42, got %d", list.head.Value)
	}
	if list.tail.Value != 100 {
		t.Errorf("Expected tail value 100, got %d", list.tail.Value)
	}
	if list.head.Next == nil {
		t.Error("Head should have Next pointer after pushing second element")
	}
	if list.head.Next != list.tail {
		t.Error("Head.Next should point to tail")
	}

	// Test pushing third element
	list.Push(200)
	if list.tail.Value != 200 {
		t.Errorf("Expected tail value 200, got %d", list.tail.Value)
	}
	if list.head.Next.Next != list.tail {
		t.Error("Second element should point to tail")
	}
}

func TestLinkedList_ForEach(t *testing.T) {
	list := InitLinkedList[int]()

	// Test empty list
	count := 0
	list.ForEach(func(index int, value int) {
		count++
	})
	if count != 0 {
		t.Errorf("Expected 0 iterations for empty list, got %d", count)
	}

	// Test single element
	list.Push(42)
	var capturedIndex int
	var capturedValue int
	list.ForEach(func(index int, value int) {
		capturedIndex = index
		capturedValue = value
	})
	if capturedIndex != 0 {
		t.Errorf("Expected index 0, got %d", capturedIndex)
	}
	if capturedValue != 42 {
		t.Errorf("Expected value 42, got %d", capturedValue)
	}

	// Test multiple elements
	list.Push(100)
	list.Push(200)

	values := []int{}
	indices := []int{}
	list.ForEach(func(index int, value int) {
		indices = append(indices, index)
		values = append(values, value)
	})

	expectedValues := []int{42, 100, 200}
	expectedIndices := []int{0, 1, 2}

	if len(values) != len(expectedValues) {
		t.Errorf("Expected %d values, got %d", len(expectedValues), len(values))
	}
	for i, expected := range expectedValues {
		if values[i] != expected {
			t.Errorf("Expected value %d at index %d, got %d", expected, i, values[i])
		}
	}
	for i, expected := range expectedIndices {
		if indices[i] != expected {
			t.Errorf("Expected index %d at position %d, got %d", expected, i, indices[i])
		}
	}
}

func TestLinkedList_GenericTypes(t *testing.T) {
	// Test with string type
	stringList := InitLinkedList[string]()
	stringList.Push("hello")
	stringList.Push("world")

	stringValues := []string{}
	stringList.ForEach(func(index int, value string) {
		stringValues = append(stringValues, value)
	})

	expectedStrings := []string{"hello", "world"}
	if len(stringValues) != len(expectedStrings) {
		t.Errorf("Expected %d string values, got %d", len(expectedStrings), len(stringValues))
	}
	for i, expected := range expectedStrings {
		if stringValues[i] != expected {
			t.Errorf("Expected string '%s' at index %d, got '%s'", expected, i, stringValues[i])
		}
	}

	// Test with struct type
	type Person struct {
		Name string
		Age  int
	}

	structList := InitLinkedList[Person]()
	structList.Push(Person{"Alice", 30})
	structList.Push(Person{"Bob", 25})

	structValues := []Person{}
	structList.ForEach(func(index int, value Person) {
		structValues = append(structValues, value)
	})

	if len(structValues) != 2 {
		t.Errorf("Expected 2 struct values, got %d", len(structValues))
	}
	if structValues[0].Name != "Alice" || structValues[0].Age != 30 {
		t.Errorf("First struct value incorrect: %+v", structValues[0])
	}
	if structValues[1].Name != "Bob" || structValues[1].Age != 25 {
		t.Errorf("Second struct value incorrect: %+v", structValues[1])
	}
}

func TestLinkedList_EdgeCases(t *testing.T) {
	// Test pushing zero values
	intList := InitLinkedList[int]()
	intList.Push(0)
	intList.Push(0)

	count := 0
	intList.ForEach(func(index int, value int) {
		if value != 0 {
			t.Errorf("Expected value 0, got %d", value)
		}
		count++
	})
	if count != 2 {
		t.Errorf("Expected 2 zero values, got %d", count)
	}

	// Test with nil values for pointer types
	ptrList := InitLinkedList[*int]()
	var nilPtr *int
	ptrList.Push(nilPtr)

	ptrList.ForEach(func(index int, value *int) {
		if value != nil {
			t.Error("Expected nil pointer value")
		}
	})
}

func TestLinkedList_OrderPreservation(t *testing.T) {
	list := InitLinkedList[int]()

	// Push elements in specific order
	elements := []int{1, 2, 3, 4, 5}
	for _, elem := range elements {
		list.Push(elem)
	}

	// Verify order is preserved
	index := 0
	list.ForEach(func(i int, value int) {
		if value != elements[index] {
			t.Errorf("Expected %d at position %d, got %d", elements[index], index, value)
		}
		index++
	})

	if index != len(elements) {
		t.Errorf("Expected %d elements, got %d", len(elements), index)
	}
}
