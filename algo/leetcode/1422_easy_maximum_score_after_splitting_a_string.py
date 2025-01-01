# Daily Question: 2025-01-01
# https://leetcode.com/problems/maximum-score-after-splitting-a-string


class Solution:
    def maxScore(self, s: str) -> int:

        left_score = 0
        right_score = len([x for x in s if x == "1"])

        maximum_score = 0

        for c in s[:-1]:
            if c == "0":
                left_score += 1
            else:
                right_score -= 1

            maximum_score = max(maximum_score, (left_score + right_score))
        return maximum_score


# Time: O(n)
# Space: O(1)
