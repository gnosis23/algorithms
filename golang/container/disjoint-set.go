package container

// 并查集
// - 带高度和路径压缩
// - n 从 0 开始。 1..n 需要+1
type DisjointSet struct {
	P    []int // 父节点
	Rank []int // 树高度
}

func InitDisjointSet(n int) *DisjointSet {
	d := &DisjointSet{}
	d.P = make([]int, n)
	d.Rank = make([]int, n)
	for i := range n {
		d.P[i] = i
	}
	return d
}

func (d *DisjointSet) InSame(u, v int) bool {
	return d.FindSet(u) == d.FindSet(v)
}

func (d *DisjointSet) Join(u, v int) {
	if d.FindSet(u) != d.FindSet(v) {
		d.link(d.FindSet(u), d.FindSet(v))
	}
}

func (d *DisjointSet) FindSet(u int) int {
	if u != d.P[u] {
		d.P[u] = d.FindSet(d.P[u])
	}
	return d.P[u]
}

func (d *DisjointSet) link(u, v int) {
	if d.Rank[u] > d.Rank[v] {
		d.P[v] = u
	} else {
		d.P[u] = v
		if d.Rank[u] == d.Rank[v] {
			d.Rank[u] = d.Rank[v] + 1
		}
	}
}
