# @ 2024-12-17
# https://leetcode.com/problems/construct-string-with-repeat-limit

from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        sol = ""
        table = Counter(s)
        sorted_table = [
            [chr(x), table[chr(x)]] for x in range(122, 96, -1) if chr(x) in table
        ]

        repeat = 0
        while sorted_table:
            if repeat == repeatLimit:
                if len(sorted_table) == 1:
                    break
                sol += sorted_table[1][0]
                sorted_table[1][1] -= 1
                if sorted_table[1][1] == 0:
                    sorted_table.pop(1)
                repeat = 0
            else:
                sol += sorted_table[0][0]
                repeat += 1
                sorted_table[0][1] -= 1
                if sorted_table[0][1] == 0:
                    sorted_table.pop(0)
                    repeat = 0

        return sol
