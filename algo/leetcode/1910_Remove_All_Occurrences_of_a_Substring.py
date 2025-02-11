# Daily Question: 2025-02-11
# https://leetcode.com/problems/remove-all-occurrences-of-a-substring


class Solution:

    def removeOccurrences(self, s: str, part: str) -> str:

        idx = 0
        while len(s) >= len(part) and idx != -1:
            idx = s.find(part)
            if idx != -1:
                s = s[:idx] + s[idx + len(part) :]

        return s


# Time: O(n^2) where n is the length of s (its n^2 because find is O(n))
# Space: O(1)


# by https://leetcode.com/problems/remove-all-occurrences-of-a-substring/solutions/2494400/python-easy-solution/?envType=daily-question&envId=2025-02-11
class Solution:

    def removeOccurrences(self, s: str, part: str) -> str:

        while part in s:
            s = s.replace(part, "", 1)
        return s


# Time: O(n^2) where n is the length of s (its n^2 because replace is O(n))
# Space: O(1)
