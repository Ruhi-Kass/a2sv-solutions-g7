class Solution:
    def diffWaysToCompute(self, expression):
        memo = {}
        
        def compute(s):
            if s in memo:
                return memo[s]
            
    
            if s.isdigit():
                memo[s] = [int(s)]
                return memo[s]
            
            res = []
            
        
            for i, char in enumerate(s):
                if char in '+-*':
                    left_results = compute(s[:i])
                    right_results = compute(s[i+1:])
                    
                    for left in left_results:
                        for right in right_results:
                            if char == '+':
                                res.append(left + right)
                            elif char == '-':
                                res.append(left - right)
                            else:  
                                res.append(left * right)
            
            memo[s] = res
            return res
        
        return compute(expression)
