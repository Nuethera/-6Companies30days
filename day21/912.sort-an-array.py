#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left,right):
            l,r,i,j=len(left),len(right),0,0
            ans=[]
            while i<l and j<r:
                if left[i]<right[j]:
                    ans.append(left[i])
                    i+=1
                else:
                    ans.append(right[j])
                    j+=1
            while i<l:
                ans.append(left[i])
                i+=1
                
            while j<r:
                ans.append(right[j])
                j+=1
            return ans
        def mergeSort(nums,lo,high):
            if lo==high:
                return [nums[lo]]
            mid=(lo+high)//2
            left=mergeSort(nums,lo,mid)
            right=mergeSort(nums,mid+1,high)
            return merge(left,right)
        return mergeSort(nums,0,len(nums)-1)
        
# @lc code=end

