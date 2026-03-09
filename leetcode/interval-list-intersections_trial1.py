from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i = 0
        j = 0
        
        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]
            
           
            inter_start = max(start1, start2)
            inter_end   = min(end1, end2)
            
         
            if inter_start <= inter_end:
                result.append([inter_start, inter_end])
            
           
            if end1 < end2:
                i += 1
            else:
                j += 1
        
        return result