# Daily Question: 2025-01-15
# https://leetcode.com/problems/minimize-xor


class Solution:

    def minimizeXor(self, num1: int, num2: int) -> int:
        b1, b2 = bin(num1)[2:], bin(num2)[2:]
        # c1, c2 = num1.bit_count(), num2.bit_count()
        c1, c2 = b1.count("1"), b2.count("1")

        if c1 == c2:
            return num1

        elif c1 > c2:
            sol = ""
            for b in b1:
                if b == "0" or c2 == 0:
                    sol += "0"
                else:
                    sol += "1"
                    c2 -= 1

        elif c1 < c2:
            sol = ""
            c2 -= c1
            for b in b1[::-1]:
                if b == "0" and c2 != 0:
                    sol += "1"
                    c2 -= 1
                else:
                    sol += b

            sol = sol[::-1]

        return int("1" * c2 + sol, 2)


# Time: O(n)
# Space: O(1)
# Terrible solution, but it works
