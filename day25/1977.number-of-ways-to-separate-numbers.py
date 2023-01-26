#
# @lc app=leetcode id=1977 lang=python3
#
# [1977] Number of Ways to Separate Numbers
#

# @lc code=start
class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10**9 + 7       
        n = len(num)
        counts = [[0] * (n+1) for _ in range(n)]
        for i in range(n):
            counts[i][n] = 1 if num[i] != '0' else 0
        
        def less(i, j, L):
            return num[i:i+L] <= num[j:j+L]
        
        ans = counts[0][n]
        for j in range(n-1, 0, -1):
            k, total = n, 0 
            start = max(0, 2*j-k) 
            for i in range(start, j): 
                if num[i] != '0':
                    
                    while k-j > j-i or (k-j == j-i and less(i,j,j-i)):
                        total += counts[j][k]
                        total %= MOD
                        k -= 1
                        
                    counts[i][j] = total
                    
            ans += counts[0][j]
            ans %= MOD
            
        return ans
        
        
# @lc code=end

