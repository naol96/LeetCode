class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda pts : (pts[0] ** 2) + (pts[1] ** 2))
        return points[:k]

