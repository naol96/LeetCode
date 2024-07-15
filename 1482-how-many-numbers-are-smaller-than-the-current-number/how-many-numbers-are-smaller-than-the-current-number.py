class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        for index, n in enumerate(nums):
            for m in nums:
                if m<n:
                    result[index]+=1
        return result