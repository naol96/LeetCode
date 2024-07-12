class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=0
        for char in nums:
            if val != char:
                nums[j]=char 
                j+=1
        return j
