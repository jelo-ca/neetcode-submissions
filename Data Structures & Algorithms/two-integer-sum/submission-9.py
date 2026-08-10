class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            remaining = nums[i+1:]
            if target - nums[i] in remaining:
                second_idx = remaining.index(target-nums[i]) + i + 1
                return [i, second_idx]
        