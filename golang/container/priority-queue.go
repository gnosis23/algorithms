package container

type PriorityQueueItem struct {
	Value    string
	Priority int
}

// PriorityQueue 是一个最小堆实现的优先队列
// 小的优先级在前
type PriorityQueue struct {
	items []*PriorityQueueItem
}

// InitPriorityQueue 创建一个新的优先队列
func InitPriorityQueue() *PriorityQueue {
	return &PriorityQueue{
		items: make([]*PriorityQueueItem, 0),
	}
}

// Len 返回队列中元素的数量
func (pq *PriorityQueue) Len() int {
	return len(pq.items)
}

// Push 向队列中添加一个元素
func (pq *PriorityQueue) Push(value string, priority int) {
	item := &PriorityQueueItem{Value: value, Priority: priority}
	pq.items = append(pq.items, item)
	pq.up(pq.Len() - 1)
}

// Pop 移除并返回优先级最小的元素
func (pq *PriorityQueue) Pop() *PriorityQueueItem {
	if pq.Len() == 0 {
		return nil
	}

	n := pq.Len() - 1
	pq.swap(0, n)
	pq.down(0, n)

	item := pq.items[n]
	pq.items = pq.items[:n]
	return item
}

// Peek 返回优先级最小的元素但不移除
func (pq *PriorityQueue) Peek() *PriorityQueueItem {
	if pq.Len() == 0 {
		return nil
	}
	return pq.items[0]
}

// IsEmpty 检查队列是否为空
func (pq *PriorityQueue) IsEmpty() bool {
	return pq.Len() == 0
}

// Update 更新指定元素的优先级
func (pq *PriorityQueue) Update(value string, newPriority int) bool {
	for i, item := range pq.items {
		if item.Value == value {
			oldPriority := item.Priority
			item.Priority = newPriority
			if newPriority < oldPriority {
				pq.up(i)
			} else {
				pq.down(i, pq.Len())
			}
			return true
		}
	}
	return false
}

// Remove 移除指定值的元素
func (pq *PriorityQueue) Remove(value string) bool {
	for i, item := range pq.items {
		if item.Value == value {
			n := pq.Len() - 1
			if n != i {
				pq.swap(i, n)
				pq.down(i, n)
				if pq.items[i].Priority == pq.items[n].Priority {
					pq.up(i)
				}
			}
			pq.items = pq.items[:n]
			return true
		}
	}
	return false
}

// 堆操作辅助方法
func (pq *PriorityQueue) up(j int) {
	for {
		parent := (j - 1) / 2
		if parent == j || !pq.less(j, parent) {
			break
		}
		pq.swap(parent, j)
		j = parent
	}
}

func (pq *PriorityQueue) down(i0, n int) bool {
	i := i0
	for {
		j1 := 2*i + 1
		if j1 >= n || j1 < 0 { // j1 < 0 after int overflow
			break
		}
		j := j1 // left child
		if j2 := j1 + 1; j2 < n && pq.less(j2, j1) {
			j = j2 // = 2*i + 2  // right child
		}
		if !pq.less(j, i) {
			break
		}
		pq.swap(i, j)
		i = j
	}
	return i > i0
}

func (pq *PriorityQueue) less(i, j int) bool {
	return pq.items[i].Priority < pq.items[j].Priority
}

func (pq *PriorityQueue) swap(i, j int) {
	pq.items[i], pq.items[j] = pq.items[j], pq.items[i]
}
