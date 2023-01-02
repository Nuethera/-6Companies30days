#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        x=0
        y=0
        f = {}
        for i in secret:
            if i not in f:
                f[i]=0
            f[i]+=1
        for i in range(len(secret)):
            if guess[i] in f:
                if f[guess[i]]>0:
                    if secret[i] == guess[i]:
                        x+=1
                    else:
                        y+=1
                    f[guess[i]] -= 1
                else:
                    if secret[i] == guess[i]:
                        x+=1
                        y-=1
            
        return f"{x}A{y}B"
# @lc code=end

