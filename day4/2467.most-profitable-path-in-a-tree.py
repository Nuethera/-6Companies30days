#
# @lc app=leetcode id=2467 lang=python3
#
# [2467] Most Profitable Path in a Tree
#

# @lc code=start
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adjList = [[] for _ in range(len(amount))]
        for u,v in edges :
            adjList[u].append(v)
            adjList[v].append(u)
        n = len(amount)
        time = [0] * n
        time[bob] = 1

        def dfs1(node,par):
            if node == bob:
                return time[bob]
            
            res = 0
            for adj in adjList[node]:
                if adj == par:
                    continue
                flag = dfs1(adj,node)
                if flag!=0:
                    res = 1 + flag
            time[node]=res
            return res
        dfs1(0,None)
        print(time)
        
        self.a = float("-inf")
        def dfs2(node,par,t,pro):
            for i in adjList[node]:
                if i==par:
                    continue
                nt = t+1
                np = pro  
                if time[i] == 0 or nt < time[i]:
                    np += amount[i]
                elif nt == time[i]:
                    np += amount[i]/2
                if len(adjList[i] )== 1:
                    self.a = max(self.a,np)
                dfs2(i,node,nt,np)

        dfs2(0,None,1,amount[0])
        return int(self.a)

        
# @lc code=end

