#
# @lc app=leetcode id=1169 lang=python3
#
# [1169] Invalid Transactions
#

# @lc code=start
class Solution:
    def invalidTransactions(self, tran: List[str]) -> List[str]:
        txn = defaultdict(list)
        ans = []
        for i in tran:
            n, t, a, c = i.split(",")
            txn[n].append([t,a,c])

        for i in tran:
            n, t, a, c = i.split(",")
            if int(a)>1000:
                ans.append(i)
            else:
                for j in txn[n]:
                    ti,ai,ci = j
                    if c != ci and abs(int(t)-int(ti)) <= 60:
                        ans.append(i)
                        break
            
        return ans
        
# @lc code=end

