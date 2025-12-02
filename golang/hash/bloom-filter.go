package hash

import (
	"hash/fnv"
	"math"
)

type BloomFilter struct {
	m    uint // size of bit array
	k    uint // number of hash
	bits []bool
}

// NewBloomFilter 根据期望元素数(预计添加元素数) n 和误判率 p 创建
func NewBloomFilter(n uint, p float64) *BloomFilter {
	// 1. 计算数组大小
	//   m = -(n * ln p) / (ln 2)^2
	// eg:
	//   n=100_000 p=0.01  m=958505
	//   n=100_000 p=0.001 m=1437848
	mFloat := -float64(n) * math.Log(p) / (math.Ln2 * math.Ln2)
	m := uint(math.Ceil(mFloat))

	// 2. 计算最优的哈希函数个数 k
	//   k = (m / n) * ln 2
	// eg:
	//   n=100_000 k=9.9
	kFloat := mFloat / float64(n) * math.Ln2
	k := uint(math.Ceil(kFloat))

	// 确保 m 和 k 至少为 1
	if m == 0 {
		m = 1
	}
	if k == 0 {
		k = 1
	}

	// fmt.Printf("--- 布隆过滤器参数计算结果 ---\n")
	// fmt.Printf("期望元素数 (n): %d\n", n)
	// fmt.Printf("目标误判率 (p): %.4f%%\n", p*100)
	// fmt.Printf("最优位数组大小 (m): %d bits\n", m)
	// fmt.Printf("最优哈希函数个数 (k): %d\n", k)
	// fmt.Printf("----------------------------------\n")

	return &BloomFilter{
		m:    m,
		k:    k,
		bits: make([]bool, m), // 使用 []bool 数组模拟位数组，虽然效率不如 BitSet 但更简洁
	}
}

// 两个基础哈希函数，用于生成 k 个哈希索引。
// 由于我们需要 k 个独立的哈希函数，通常采用双重哈希 (Double Hashing) 的技巧：
// g_i(x) = (h1(x) + i * h2(x)) mod m

// fnv: https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function
func hash1(data []byte) uint32 {
	h := fnv.New32()
	h.Write(data)
	return h.Sum32()
}

func hash2(data []byte) uint32 {
	h := fnv.New32a()
	h.Write(data)
	return h.Sum32()
}

// getIndices 使用双重哈希，生成 k 个在 [0, m-1] 范围内的索引
func (bf *BloomFilter) getIndices(data []byte) []uint {
	indices := make([]uint, bf.k)
	h1 := hash1(data)
	h2 := hash2(data)

	// 使用 (h1 + i * h2) mod m 的公式来生成 k 个哈希索引
	for i := uint(0); i < bf.k; i++ {
		// uint(h1 + i * h2) 可能会溢出，但 Go 会自动处理，我们只需要关注取模操作
		// 使用 uint32 保证兼容性
		index := (uint32(h1) + uint32(i)*uint32(h2)) % uint32(bf.m)
		indices[i] = uint(index)
	}
	return indices
}

// Add 将元素添加到布隆过滤器
func (bf *BloomFilter) Add(data []byte) {
	indices := bf.getIndices(data)
	for _, index := range indices {
		bf.bits[index] = true
	}
}

// Check 检查元素是否可能存在于布隆过滤器中
// 返回 true 表示可能存在 (可能为误判)，返回 false 表示一定不存在
func (bf *BloomFilter) Check(data []byte) bool {
	indices := bf.getIndices(data)
	for _, index := range indices {
		// 只要有一个位是 0，则该元素一定不存在
		if !bf.bits[index] {
			return false
		}
	}
	// 所有 k 个位都是 1，则可能存在
	return true
}
