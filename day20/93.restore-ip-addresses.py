#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def backtrack(i,adr):
            
            if i==len(s):
                if len(adr)==4:
                    res.append( '.'.join(map(str,adr)) )
                return
            
            if adr[-1]!=0 and adr[-1]*10+int(s[i]) <= 255:
                lastItem = adr[-1]
                adr[-1] = lastItem*10+int(s[i]) 
                backtrack(i+1, adr)
                adr[-1] = lastItem 
            
           
            if len(adr)<4:
                adr.append(int(s[i]))
                backtrack(i+1,adr)         
                adr.pop() 
        
        backtrack(1,[int(s[0])])
        return res
        
# @lc code=end

