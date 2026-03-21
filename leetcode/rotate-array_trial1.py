class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n                 
        if k == 0:
            return
      
        nums.reverse()
        
        nums[:k] = nums[:k][::-1]
        
        nums[k:] = nums[k:][::-1]