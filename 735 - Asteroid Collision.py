class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
    
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                break
            else:   # this else block is assosiated with while not with if
                stack.append(asteroid)
        return stack
