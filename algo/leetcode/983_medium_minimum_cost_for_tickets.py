# Daily Question: 2024-12-31
# https://leetcode.com/problems/minimum-cost-for-tickets

from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        table = {day: i for i, day in enumerate(days)} | {0: -1}

        all_days = []
        for i, j in zip(([0] + days)[:-1], ([0] + days)[1:]):
            all_days += [table[i] for _ in range(i, j)]

        dp = [0]
        for day in days:
            opt_cost = min(
                [
                    min(dp[all_days[max(day - d, 0)] + 1 :]) + costs[i]
                    for i, d in enumerate([1, 7, 30])
                ]
            )
            dp.append(opt_cost)

        return dp[-1]


# Time: O(n) -> 7ms Beat 44.54%
# Space: O(n) -> 17.91MB Beats 17.91%
# where n is the number of days
