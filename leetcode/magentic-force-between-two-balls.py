from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        
        def can_place(force: int) -> bool:
            count = 1
            last = position[0]
            for i in range(1, n):
                if position[i] - last >= force:
                    count += 1
                    last = position[i]
                    if count >= m:
                        return True
            return count >= m
        
        left = 1
        right = position[-1] - position[0]
        
        while left < right:
            mid = (left + right + 1) // 2
            if can_place(mid):
                left = mid
            else:
                right = mid - 1
        
        return left
