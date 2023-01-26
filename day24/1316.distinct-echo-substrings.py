#
# @lc app=leetcode id=1316 lang=python3
#
# [1316] Distinct Echo Substrings
#

# @lc code=start
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        sub = set()
        for le in range(1, (len(s)//2)+1):
            l=0
            r=le
            count = 0
            while l<len(s)-le:
                if s[l] == s[r]: count+=1
                else: count=0

                if count==le:
                    sub.add(s[l-le+1:l+1])
                    count-=1

                l+=1
                r+=1
        
        return len(sub)
            
        
# @lc code=end

