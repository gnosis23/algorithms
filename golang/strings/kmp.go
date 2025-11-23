package strings

// find index of substr in str, -1 if not exist
func kmp(str, substr string) int {
	if len(substr) == 0 {
		return 0
	}
	if len(str) == 0 {
		return -1
	}

	// Build prefix table (also known as failure function or LPS - Longest Prefix Suffix)
	prefixTable := buildPrefixTable(substr)

	i, j := 0, 0
	for i < len(str) {
		if str[i] == substr[j] {
			i++
			j++
			if j == len(substr) {
				return i - j
			}
		} else {
			if j > 0 {
				j = prefixTable[j-1]
			} else {
				i++
			}
		}
	}

	return -1
}

// buildPrefixTable constructs the prefix table for KMP algorithm
func buildPrefixTable(pattern string) []int {
	n := len(pattern)
	prefixTable := make([]int, n)
	length := 0
	i := 1

	for i < n {
		if pattern[i] == pattern[length] {
			length++
			prefixTable[i] = length
			i++
		} else {
			if length != 0 {
				length = prefixTable[length-1]
			} else {
				prefixTable[i] = 0
				i++
			}
		}
	}

	return prefixTable
}
