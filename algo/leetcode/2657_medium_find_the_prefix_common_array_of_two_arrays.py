# Daily Question: 2025-01-14
# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays

from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        setA, setB, sol = set(), set(), [0]

        for idx, (a, b) in enumerate(zip(A, B)):
            sol.append(sol[idx])

            if a == b:
                sol[-1] += 1
                continue

            setA.add(a)
            setB.add(b)

            sol[-1] = sol[-1] + 1 if a in setB else sol[-1]
            sol[-1] = sol[-1] + 1 if b in setA else sol[-1]

        return sol[1:]


# Time: O(n)
# Space: O(n)
