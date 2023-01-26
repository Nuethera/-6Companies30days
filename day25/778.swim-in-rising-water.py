#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#

# @lc code=start
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minH = [[grid[0][0],0,0]]
        direc = [[1,0],[-1,0],[0,1],[0,-1]]
        visit.add((0,0))


        while minH:
            t,r,c = heappop(minH)
            if r==n-1 and c==n-1:
                return t
            
            for di,dj in direc:
                nr,nc = r+di,c+dj
                if nr in (-1,n) or nc in (-1,n) or (nr,nc) in visit:
                    continue
                visit.add((nr,nc))
                heappush(minH, [max(t,grid[nr][nc]),nr,nc])
        
        
# @lc code=end

