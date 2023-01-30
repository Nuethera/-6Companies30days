#
# @lc app=leetcode id=1856 lang=python3
#
# [1856] Maximum Subarray Min-Product
#

# @lc code=start
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        n=len(nums)
        prefix_sum = [0]*(n+1)
        right = [n] * n
        left = [-1] * n
        st = []
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        for i in range(n):
            while st and nums[i] <= nums[st[-1]]:
                st.pop()
            
            if not st:
                left[i] = -1
            else:
                left[i] = st[-1]
            st.append(i)
        st = []
        for i in range(n-1,-1,-1):
            while st and nums[i] <= nums[st[-1]]:
                st.pop()
            
            if not st:
                right[i] = n
            else:
                right[i] = st[-1]
            st.append(i)

        ans = 0
        for i in range(n):
            l = left[i]
            r = right[i]
            s = prefix_sum[r] - prefix_sum[l+1]
            p = s * nums[i]
            ans = max(ans,p)

        return ans % MOD
        
# @lc code=end

