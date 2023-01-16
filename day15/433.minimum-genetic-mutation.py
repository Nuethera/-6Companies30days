#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#

# @lc code=start
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        q = collections.deque([(startGene,0)])
        while q:
            g, m = q.popleft()
            if g==endGene:
                return m
            
            for i in range(8):
                for s in "ACGT":
                    gm = g[:i] + s + g[i+1:]
                    if gm in bank:
                        bank.remove(gm)
                        q.append((gm,m+1))
            
        return -1
        
# @lc code=end

