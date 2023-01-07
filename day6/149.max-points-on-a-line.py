#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        h = defaultdict(set)
        for i in range(len(points)):
            u1,v1 = points[i]
            for j in range(len(points)):
                if i==j:
                    continue
                u2,v2 = points[j]
                try:
                    m=(v2-v1)/(u2-u1)
                    c = v1 - m*u1
                except ZeroDivisionError:
                    m = float('inf')
                    c=u1
                    
                h[m,c].add(tuple(points[i]))
                h[m,c].add(tuple(points[j]))

        M=-1
        for i in list(h.values()):
            M = max(M,len(i))
        return M
# @lc code=end

