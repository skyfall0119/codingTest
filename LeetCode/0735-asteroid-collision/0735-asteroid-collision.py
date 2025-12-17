class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        for ast in asteroids:
            if ast < 0:
                if not stack:
                    stack.append(ast)
                    continue
                
                while stack and stack[-1] > 0: 
                    if abs(stack[-1]) > abs(ast):
                        break
                    if abs(stack[-1]) == abs(ast):
                        stack.pop()
                        break
                    # ast bigger
                    stack.pop()
                    
                else:
                    stack.append(ast)
            
            else:
                stack.append(ast)

        return stack
        

