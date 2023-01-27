#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k+1):
            t = prices.copy()
            for s,d,c in flights:
                if prices[s] == float('inf'): continue
                if t[d] > prices[s]+c:
                    t[d] = prices[s]+c
            
            prices = t

        if prices[dst] == float('inf'):
            return -1
        return prices[dst]
        
# @lc code=end

