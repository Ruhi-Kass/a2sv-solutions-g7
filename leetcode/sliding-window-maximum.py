from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        result = []
        dq = deque() 
        
        for i in range(len(nums)):
        
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)
            

            if dq[0] == i - k:
                dq.popleft()
            
            
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result
