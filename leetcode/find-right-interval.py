class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
       
        start_to_idx = {start: i for i, (start, end) in enumerate(intervals)}
        
        
        starts = sorted((start, idx) for start, idx in start_to_idx.items())
        
        def find_right(end: int) -> int:
            
            left, right = 0, len(starts) - 1
            while left <= right:
                mid = (left + right) // 2
                if starts[mid][0] >= end:
                    right = mid - 1
                else:
                    left = mid + 1
            return starts[left][1] if left < len(starts) else -1
        
        return [find_right(end) for _, end in intervals]
