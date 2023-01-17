#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d=defaultdict(int)
        for a in words:
            d[a]+=1
        arr=[]
        for a in d:
            arr.append((d[a],a))
        arr.sort(key=lambda x:(1/x[0],x[1]))
        ans=[]
        for i in range(k):
            ans.append(arr[i][1])
        return ans
        
# @lc code=end

