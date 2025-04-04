from typing import List
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res =0
        
        left= nums[0]
        N=len(nums)
        for j in range(1,N):
            if left<nums[j]:
                left=nums[j]
            for k in range(j+1,N):
                res= max(res, (left-nums[j]) * nums[k])
        return res
            