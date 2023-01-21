#
# @lc app=leetcode id=1095 lang=python3
#
# [1095] Find in Mountain Array
#

# @lc code=start
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:
        n = arr.length()
        l,r=0,n-1

        while l<r:
            m = (l+r)//2
            if arr.get(m)<arr.get(m+1):

                l=peak = m+1
            else:
                r=m
        
        l,r= 0,peak
        while l<=r:
            m = (l+r)//2
            t = arr.get(m)
            if t < target:
                l = m+1
            elif t > target:
                r = m-1
            else:
                return m
        l, r = peak, n - 1
        while l <= r:
            m = (l + r) // 2
            t = arr.get(m)
            if t > target:
                l = m + 1
            elif t < target:
                r = m - 1
            else:
                return m
        return -1
        
# @lc code=end

