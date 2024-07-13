class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ind=0    
        for i in nums:
            if i==target:
                ret=ind
            elif i < target:
                ind+=1
            ret=ind        
        return ret

