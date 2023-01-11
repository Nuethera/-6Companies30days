#
# @lc app=leetcode id=1878 lang=python3
#
# [1878] Get Biggest Three Rhombus Sums in a Grid
#

# @lc code=start
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m=len(grid)
        n = len(grid[0])
        def calc(l,r,i,d):
            ssum = 0
            c1=c2=(l+r) // 2
            ex = True
            for r in range(i,d+1):
                if c1 == c2:
                    ssum += grid[r][c1]
                else:
                    ssum += grid[r][c1] + grid[r][c2]
                
                if c1 == l:
                    ex = False
                if ex:
                    c1-=1
                    c2+=1
                else:
                    c1+=1
                    c2-=1

            return ssum
        a = []
        for i in range(m):
            for j in range(n):
                l=r=j
                d=i 
                while l>=0 and r<n and d<m:
                    ssum = calc(l,r,i,d)
                    d+=2
                    l-=1
                    r+=1
                    if len(a)<3:
                        if ssum not in a:
                            heappush(a,ssum)
                    else:
                        if ssum not in a and ssum > a[0]:
                            heappop(a)
                            heappush(a,ssum)

        a.sort(reverse=True)

        return a
        
# @lc code=end

