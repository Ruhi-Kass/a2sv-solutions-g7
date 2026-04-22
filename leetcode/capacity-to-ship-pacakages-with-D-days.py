from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canShip(capacity):
            day_count = 1
            current_load = 0
            
            for w in weights:
                if current_load + w > capacity:
                    day_count += 1
                    current_load = 0
                current_load += w
            
            return day_count <= days
        
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            
            if canShip(mid):
                right = mid  
            else:
                left = mid + 1
        
        return left
