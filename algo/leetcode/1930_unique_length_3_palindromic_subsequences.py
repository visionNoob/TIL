# Daily Question: 2025-01-04
# https://leetcode.com/problems/unique-length-3-palindromic-subsequences

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        table = dict()

        for idx, c in enumerate(s):
            table[c] = [table.get(c, [idx, idx])[0], idx]

        sol = 0
        for start, end in table.values():
            sol += len(set(s[start + 1 : end])) if end - start >= 2 else 0

        return sol


# Time: O(n) where n is the length of the string
# Space: O(n) 