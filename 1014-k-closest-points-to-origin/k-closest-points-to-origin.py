class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        output = []
        for items in points:
            dist = math.sqrt(items[0]**2 + items[1]**2)
            distance.append((dist, items))
        distance.sort(key=lambda x: x[0])
        for item in distance[:k]:
            output.append(item[1])
        return output

