# Daily Question: 2025-01-11
# https://leetcode.com/problems/construct-k-palindrome-strings

from collections import Counter, defaultdict


# Method 1
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        table = set()
        for c in s:
            if c in table:
                table.remove(c)
            else:
                table.add(c)

        return sum(table.values()) <= k


# Method 2
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        table = defaultdict(bool)

        for c in s:
            table[c] = not table[c]

        if sum(table.values()) <= k:
            return True

        return False


# Method 3 -> Fastest
# Counter is faster than defaultdict because it is implemented in C
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return sum(v & 1 for v in Counter(s).values()) <= k <= len(s)


# Time: O(n)
# Space: O(1)
