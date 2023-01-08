#
# @lc app=leetcode id=447 lang=python3
#
# [447] Number of Boomerangs
#

# @lc code=start
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        dist = lambda a,b:(a[1]-b[1])**2 + (a[0]-b[0])**2

        h = defaultdict(dict)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                d = dist(points[i],points[j])
                if d not in h[i]:
                    h[i][d] = []
                if d not in h[j]:
                    h[j][d] = []
                h[i][d].append(j)
                h[j][d].append(i)
        a = 0
        for i in list(h.values()):
            for j in list(i.values()):
                l = len(j)
                if l >= 2:

                    a += l *(l -1)

        return a
        
# @lc code=end

