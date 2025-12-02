package hash

import (
	"testing"
)

func TestBloomFilter(t *testing.T) {
	// 期望参数
	const n uint = 10000    // 期望存储 10,000 个 URL
	const p float64 = 0.001 // 误判率 0.1%

	filter := NewBloomFilter(n, p)

	urls := [][]byte{
		[]byte("https://example.com/pageA"),
		[]byte("https://example.com/pageB"),
		[]byte("https://example.com/pageA"), // 重复 URL
		[]byte("https://another.com/index"),
		[]byte("https://example.com/pageB"), // 重复 URL
		[]byte("https://unique.org/path"),
	}

	// 记录已添加的URL，用于验证
	addedURLs := make(map[string]bool)
	expectedResults := make([]bool, len(urls))

	// 遍历 URL 列表
	for i, url := range urls {
		urlStr := string(url)

		// 检查 URL 是否存在
		if filter.Check(url) {
			// 如果可能重复，则不添加
			expectedResults[i] = true
			t.Logf("[可能重复] URL: %s", urlStr)
		} else {
			// 如果一定不存在，则添加并标记为新 URL
			filter.Add(url)
			addedURLs[urlStr] = true
			expectedResults[i] = false
			t.Logf("[新 URL]    URL: %s", urlStr)
		}
	}

	// 验证添加逻辑：新URL应该被添加，重复URL不应该被重复添加
	expectedAddedCount := 4 // pageA, pageB, another.com/index, unique.org/path
	if len(addedURLs) != expectedAddedCount {
		t.Errorf("添加的URL数量不正确: 期望 %d, 实际 %d", expectedAddedCount, len(addedURLs))
	}

	// 验证一个已知的新 URL (期待返回 false)
	nonExistentURL := []byte("https://definitely.not.seen/yet")
	if filter.Check(nonExistentURL) {
		t.Errorf("发生误判 (False Positive): 查询 URL: %s 结果应为 false, 实际为 true", string(nonExistentURL))
	} else {
		t.Logf("[结果正确] 查询 URL: %s 结果：一定不存在。", string(nonExistentURL))
	}

	// 验证一个已知已添加的 URL (期待返回 true)
	existingURL := []byte("https://another.com/index")
	if !filter.Check(existingURL) {
		t.Errorf("发生假阴性 (False Negative): 查询 URL: %s 结果应为 true, 实际为 false", string(existingURL))
	} else {
		t.Logf("[结果正确] 查询 URL: %s 结果：可能存在。", string(existingURL))
	}

	// 验证所有已添加的URL都应该返回true
	for urlStr := range addedURLs {
		if !filter.Check([]byte(urlStr)) {
			t.Errorf("已添加的URL检查失败: %s 应该返回 true", urlStr)
		}
	}
}
