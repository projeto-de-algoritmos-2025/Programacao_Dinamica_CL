from typing import List
from functools import lru_cache

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(i: int, j: int, k: int) -> int:
            if i > j:
                return 0
            
            while i + 1 <= j and boxes[i] == boxes[i + 1]:
                i += 1
                k += 1

            res = dp(i + 1, j, 0) + (k + 1) ** 2

            for m in range(i + 1, j + 1):
                if boxes[m] == boxes[i]:
                    res = max(res, dp(i + 1, m - 1, 0) + dp(m, j, k + 1))
            
            return res
        
        return dp(0, len(boxes) - 1, 0)
