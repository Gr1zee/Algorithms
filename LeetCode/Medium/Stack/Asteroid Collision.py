class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if ast < 0:
                while stack and abs(ast) > stack[-1] and stack[-1] > 0:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(ast)
                if abs(ast) == stack[-1]:
                    stack.pop()
            else:
                stack.append(ast)
        return stack
