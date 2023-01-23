#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        i = 0
        for j in range(len(fruits)):
            count[fruits[j]] = count.get(fruits[j],0) + 1
            if len(count)>2:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0: del count[fruits[i]]
                i+=1

        print(i,j)
        return j-i+1
        
# @lc code=end

