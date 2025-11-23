package container

// 树状数组
// 数组中的元素储存在[1, n]
type BinaryIndexedTree struct {
	n    int
	data []int
}

func InitBinaryIndexedTree(n int) *BinaryIndexedTree {
	bit := &BinaryIndexedTree{}
	bit.n = n
	bit.data = make([]int, n+1)
	return bit
}

// 统计前n个数之和 (n从1开始)
func (x *BinaryIndexedTree) Sum(n int) int {
	sum := 0
	for n > 0 {
		sum += x.data[n]
		n = n & (n - 1)
	}
	return sum
}

// 给第i个元素+a (i从0开始)
func (x *BinaryIndexedTree) Add(i, a int) {
	// 为了方便起见，i从0开始
	n := i + 1
	for n <= x.n {
		x.data[n] += a
		n += n & -n
	}
}
