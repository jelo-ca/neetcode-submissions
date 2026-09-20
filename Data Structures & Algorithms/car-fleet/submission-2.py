class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Keep a stack of estimated arrival. 
        stack = []

        # kv of pos and speed
        pos = {}

        for i in range(len(position)):
            pos[position[i]] = speed[i]

        for p in sorted(pos.keys()):
            arrival = (target - p) / pos[p]

            # print(p, stack)

            # if prev arrival <= curr, prev joins fleet
            while stack and stack[-1] <= arrival:
                stack.pop()

            stack.append(arrival)

        return len(stack)
        # sort pairs -> based off position

        