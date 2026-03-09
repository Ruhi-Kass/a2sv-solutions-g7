from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        
       
        zeros = 0
        for num in arr:
            if num == 0:
                zeros += 1
        
      
        i = n - 1        
        j = n + zeros - 1 
        
        while i >= 0:
            if j < n:
                arr[j] = arr[i]
            j -= 1
            
            if arr[i] == 0:
                if j < n:
                    arr[j] = 0
                j -= 1
            
            i -= 1