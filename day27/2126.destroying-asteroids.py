#
# @lc app=leetcode id=2126 lang=python3
#
# [2126] Destroying Asteroids
#

# @lc code=start
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for k in asteroids:
            if k>mass:
                return False
            
            mass+=k
        return True
        
# @lc code=end

