from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0:
                top = stack[-1]
                
                if top < abs(ast):
                    stack.pop()       
                    continue         
                
                elif top == abs(ast):
                    stack.pop()        
                    break
                
                else:
                    break
            else:
                
                stack.append(ast)
        
        return stack
