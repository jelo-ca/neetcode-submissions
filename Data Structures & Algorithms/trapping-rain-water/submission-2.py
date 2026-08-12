class Solution:
    def trap(self, height: List[int]) -> int:
        p1, p2 = 0, len(height) - 1
        l_max, r_max = 0, 0
        water = 0

        while p1 != p2:
            if l_max >= r_max:
                if height[p2] > r_max:
                    r_max = height[p2]
                else:
                    water += r_max - height[p2]
                    p2 -= 1
            else:
                if height[p1] > l_max:
                    l_max = height[p1]
                else:
                    water += l_max - height[p1]
                    p1 += 1
        return water
                
                

            

