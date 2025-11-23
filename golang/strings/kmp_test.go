package strings

import (
	"testing"
)

func TestKMP(t *testing.T) {
	tests := []struct {
		name     string
		str      string
		substr   string
		expected int
	}{
		{
			name:     "empty substring",
			str:      "hello",
			substr:   "",
			expected: 0,
		},
		{
			name:     "empty string",
			str:      "",
			substr:   "abc",
			expected: -1,
		},
		{
			name:     "exact match",
			str:      "hello",
			substr:   "hello",
			expected: 0,
		},
		{
			name:     "substring at beginning",
			str:      "hello world",
			substr:   "hello",
			expected: 0,
		},
		{
			name:     "substring in middle",
			str:      "hello world",
			substr:   "world",
			expected: 6,
		},
		{
			name:     "substring not found",
			str:      "hello world",
			substr:   "xyz",
			expected: -1,
		},
		{
			name:     "single character match",
			str:      "hello",
			substr:   "e",
			expected: 1,
		},
		{
			name:     "repeated pattern",
			str:      "abcabcabc",
			substr:   "abcabc",
			expected: 0,
		},
		{
			name:     "pattern with overlapping prefixes",
			str:      "ababababca",
			substr:   "abababca",
			expected: 2,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := kmp(tt.str, tt.substr)
			if result != tt.expected {
				t.Errorf("kmp(%q, %q) = %d, expected %d", tt.str, tt.substr, result, tt.expected)
			}
		})
	}
}

func TestBuildPrefixTable(t *testing.T) {
	tests := []struct {
		pattern  string
		expected []int
	}{
		{
			pattern:  "ABCDABD",
			expected: []int{0, 0, 0, 0, 1, 2, 0},
		},
		{
			pattern:  "ABABCABAB",
			expected: []int{0, 0, 1, 2, 0, 1, 2, 3, 4},
		},
		{
			pattern:  "AAAA",
			expected: []int{0, 1, 2, 3},
		},
		{
			pattern:  "A",
			expected: []int{0},
		},
		{
			pattern:  "AAAB",
			expected: []int{0, 1, 2, 0},
		},
	}

	for _, tt := range tests {
		t.Run(tt.pattern, func(t *testing.T) {
			result := buildPrefixTable(tt.pattern)
			if len(result) != len(tt.expected) {
				t.Errorf("buildPrefixTable(%q) length = %d, expected %d", tt.pattern, len(result), len(tt.expected))
				return
			}
			for i := range result {
				if result[i] != tt.expected[i] {
					t.Errorf("buildPrefixTable(%q)[%d] = %d, expected %d", tt.pattern, i, result[i], tt.expected[i])
				}
			}
		})
	}
}