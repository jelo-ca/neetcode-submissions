class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        p1, p2 = 0, len(heights) - 1

        while p2 - p1 != 0:
            h1 = heights[p1]
            h2 = heights[p2]
            area = min(h1, h2) * (p2 - p1)

            print(area)
            if max_area < area:
                max_area = area
            
            if h1 < h2:
                p1 += 1
            else:
                p2 -= 1
        return max_area