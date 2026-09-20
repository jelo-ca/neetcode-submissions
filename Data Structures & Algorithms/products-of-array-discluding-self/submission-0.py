class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 array intialized w 1's (len = nums)
        # for loop, keep track of currprod
        # each iteration -> multiply to the index
        # do for pre & suf
        res = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        
        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]
            

        return res