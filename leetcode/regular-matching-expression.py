class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        memo = {}
        
        def dp(i: int, j: int) -> bool:
         
            if (i, j) in memo:
                return memo[(i, j)]
            
           
            if i == len(s) and j == len(p):
                return True
            
         
            if j == len(p):
                return False
            
       
            first_match = (i < len(s)) and (p[j] == '.' or p[j] == s[i])
  
            if j + 1 < len(p) and p[j + 1] == '*':
            
                result = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
         
                result = first_match and dp(i + 1, j + 1)
            
            memo[(i, j)] = result
            return result
        
        return dp(0, 0)
