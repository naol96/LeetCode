class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result=0
        for i in nums:
            counter=len(str(i))
            if counter%2==0:
                result+=1
        return result