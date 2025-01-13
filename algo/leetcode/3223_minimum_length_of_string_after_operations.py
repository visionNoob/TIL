# Daily Question: 2025-01-13
# https://leetcode.com/problems/minimum-length-of-string-after-operations

from collections import Counter


# Method 1: https://leetcode.com/problems/minimum-length-of-string-after-operations/solutions/6271284/beats-99-minimize-string-length-one-liner-python-c-hashing-solutions/?envType=daily-question&envId=2025-01-13
class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(1 if x % 2 == 1 else 2 for x in Counter(s).values())


# Method 2: my last solution
class Solution:
    def minimumLength(self, s: str) -> int:
        table = Counter(s)

        return 2 * len(table.keys()) - sum(x % 2 == 1 for x in table.values())


from collections import defaultdict


# Method 3:without using Counter -> slower
class Solution:
    def minimumLength(self, s: str) -> int:
        table = defaultdict(int)
        for c in s:
            table[c] += 1

        return 2 * len(table.keys()) - sum(x % 2 == 1 for x in table.values())


# Time: O(n)
# Space: O(1)
