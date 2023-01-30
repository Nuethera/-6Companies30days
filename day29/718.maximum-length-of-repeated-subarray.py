#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#

# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        BASE, MOD = 101, 1_000_000_000_001
        hash1, hash2, POW = [0] * (m + 1), [0] * (n + 1), [1] * (max(m, n) + 1)
        for i in range(max(m,n)): POW[i+1] = (POW[i] * BASE) % MOD
        for i in range(m): 
            hash1[i + 1] = (hash1[i] * BASE + nums1[i]) % MOD  
        for i in range(n): 
            hash2[i + 1] = (hash2[i] * BASE + nums2[i]) % MOD  


        def get_hash(h,l,r):
            return ((h[r+1] - h[l] * POW[r-l+1])%MOD + MOD)%MOD

        def foundSubArray(size):
            seen = defaultdict(list)
            for i in range(m - size + 1):
                h = get_hash(hash1, i, i + size - 1)
                seen[h].append(i)
            for i in range(n - size + 1):
                h = get_hash(hash2, i, i + size - 1)
                if h in seen:
                    for j in seen[h]:  
                        if nums1[j:j + size] == nums2[i:i + size]:
                            return True
            return False

        l,r,ans = 1, min(m, n), 0
        while l<=r:
            mid = (l+r)//2
            if foundSubArray(mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1
        
        return ans
        
# @lc code=end

