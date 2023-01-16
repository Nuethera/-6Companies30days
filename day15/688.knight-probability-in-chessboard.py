#
# @lc app=leetcode id=688 lang=python3
#
# [688] Knight Probability in Chessboard
#

# @lc code=start
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k==0:
            return 1
        d = ((-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1),
             (2, -1), (1, -2), (-1, -2))
        adjList = defaultdict(list)
        for r in range(n):
            for c in range(n):
                for di,dj in d:
                    p = (r+di,c+dj)
                    if 0 <= p[0] < n and 0 <= p[1] < n:
                        adjList[(r,c)].append(p)
        @cache
        def dfs(pos,h):
            if h == k:
                return 1
            
            res = 0
            for i in adjList[pos]:
                res += dfs(i,h+1)
            return res

        total = dfs((row,column), 0)
        
        return total / 8**k
        
# @lc code=end

