class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result=0
        for i in nums:
            counter=1
            while i > 9:
                i=int(i/10)
                counter+=1
            if counter%2==0:
                result+=1
        return result