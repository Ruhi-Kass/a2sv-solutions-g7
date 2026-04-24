class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        ans = 0
        
        for house in houses:
           
            l, r = 0, len(heaters)
            while l < r:
                m = (l + r) // 2
                if heaters[m] < house:
                    l = m + 1
                else:
                    r = m
          
            dist1 = heaters[l] - house if l < len(heaters) else float('inf')
            dist2 = house - heaters[l-1] if l > 0 else float('inf')
            ans = max(ans, min(dist1, dist2))
        
        return ans
