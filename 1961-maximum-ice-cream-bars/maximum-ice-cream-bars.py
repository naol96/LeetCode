class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        li=sorted(costs)
        sum=0
        result=0
        for i in li:
            sum+=i
            if sum <= coins:
                result+=1
            else:
                break
        return result
        