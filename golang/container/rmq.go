package container

import "math"

// RMQ 区间最小值查询
// 位置从0开始索引
type RangeMinQuery struct {
	cap  int
	data []int
}

func InitRangeMinQuery(n int) *RangeMinQuery {
	rmq := &RangeMinQuery{}

	// 容量为2的整数幂
	rmq.cap = 1
	for rmq.cap < n {
		rmq.cap *= 2
	}

	rmq.data = make([]int, 2*rmq.cap-1)
	for i := range rmq.data {
		rmq.data[i] = math.MaxInt
	}

	return rmq
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// 把第k个值(0开始)更新为a
func (x *RangeMinQuery) Update(k, a int) {
	k += x.cap - 1
	x.data[k] = a
	for k > 0 {
		k = (k - 1) / 2
		x.data[k] = min(x.data[k*2+1], x.data[k*2+2])
	}
}

// 求 [a, b)的最小值
// 后面的参数为了计算方便
// k是节点的编号，l和r表示这个节点对应的[l,r)区间
// Usage: query(a, b, 0, 0, cap)
func (x *RangeMinQuery) QueryAll(a, b int) int {
	return x.Query(a, b, 0, 0, x.cap)
}

func (x *RangeMinQuery) Query(a, b, k, l, r int) int {
	if (r <= a) || (b <= l) {
		return math.MaxInt
	}

	if (a <= l) && (r <= b) {
		return x.data[k]
	} else {
		vl := x.Query(a, b, k*2+1, l, (l+r)/2)
		vr := x.Query(a, b, k*2+2, (l+r)/2, r)
		return min(vl, vr)
	}
}
