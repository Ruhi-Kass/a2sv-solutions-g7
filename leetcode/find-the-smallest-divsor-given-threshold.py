from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if not nums:
            return 1
            
        left = 1
        right = max(nums) 
        
        while left < right:
            mid = (left + right) // 2
            
          
            total = 0
            for num in nums:
                total += (num + mid - 1) // mid   
            
            if total <= threshold:
               
                right = mid
            else:
             
                left = mid + 1
        
        return left
