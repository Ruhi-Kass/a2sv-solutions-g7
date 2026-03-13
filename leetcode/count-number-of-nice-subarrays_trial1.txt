from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most_k(k: int) -> int:
            count = 0
            left = 0
            odd_count = 0
            
            for right in range(len(nums)):
             
                if nums[right] % 2 == 1:
                    odd_count += 1
                
               
                while odd_count > k and left <= right:
                    if nums[left] % 2 == 1:
                        odd_count -= 1
                    left += 1
                
          
                count += (right - left + 1)
            
            return count
        
       
        return at_most_k(k) - at_most_k(k - 1)