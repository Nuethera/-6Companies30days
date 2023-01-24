#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        gra = {i:[] for i in range(1,n+1)}
        for s,d,w in times:
            gra[s].append((d, w))
        
        dist_map = {i:math.inf for i in range(1,n+1)}
        dist_map[k] = 0
        visited = set()
        pq = [(0,k)]
        while pq and len(visited) != n:
            t, u = heappop(pq)
            if u not in visited:
                visited.add(u)
                for v,t1 in gra[u]:
                    if v not in visited:
                        if t1+dist_map[u] < dist_map[v]:
                            dist_map[v] = t1+dist_map[u]
                            heappush(pq,(t1+dist_map[u], v))
        res = 0
        for v in dist_map.values():
            res = max(res,v)
        
        return res if res<math.inf else -1
        
# @lc code=end

