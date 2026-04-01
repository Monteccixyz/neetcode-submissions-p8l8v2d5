class Solution:
    def productExceptSelf(self, nums):
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        running = 1

        for i in range(len(nums)):
            prefix[i] = running
            running *= nums[i]
        
        running = 1

        for i in reversed(range(len(nums))):
            suffix[i] = running
            running *= nums[i]

        return [prefix[i] * suffix[i] for i in range(len(nums))]

