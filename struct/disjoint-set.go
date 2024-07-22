type DisjointSet struct {
	P    []int
	Rank []int
}

func InitDisjointSet(n int) *DisjointSet {
	d := &DisjointSet{}
	d.P = make([]int, n)
	d.Rank = make([]int, n)
	for i := 0; i < n; i++ {
		d.P[i] = i
	}
	return d
}

func (d *DisjointSet) InSame(u, v int) bool {
	return d.FindSet(u) == d.FindSet(v)
}

func (d *DisjointSet) Join(u, v int) {
	if d.FindSet(u) != d.FindSet(v) {
		d.Link(d.FindSet(u), d.FindSet(v))
	}
}

func (d *DisjointSet) FindSet(u int) int {
	if u != d.P[u] {
		d.P[u] = d.FindSet(d.P[u])
	}
	return d.P[u]
}

func (d *DisjointSet) Link(u, v int) {
	if d.Rank[u] > d.Rank[v] {
		d.P[v] = u
	} else {
		d.P[u] = v
		if d.Rank[u] == d.Rank[v] {
			d.Rank[u] = d.Rank[v] + 1
		}
	}
}
