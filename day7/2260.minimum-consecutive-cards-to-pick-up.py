#
# @lc app=leetcode id=2260 lang=python3
#
# [2260] Minimum Consecutive Cards to Pick Up
#

# @lc code=start
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        m = float('inf')
        i,j=0,0
        h = defaultdict(int)
        while j<len(cards):
            h[cards[j]] += 1
            while h[cards[j]] > 1:
                h[cards[i]] -= 1
                m = min(m,j-i+1)
                i+=1
            j+=1
        if m == float('inf'):
            return -1
        else:
            return m
        
# @lc code=end

