# Daily Question: 2024-12-18
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        for i in range(len(prices)):
            for j in range(i + 1, len(prices), 1):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        return prices


# Time: O(n^2)
# Space: O(1)
