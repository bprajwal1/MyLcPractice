class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        min_val = 2**31-1
        max_val = -2**31

        suffixMin = [0]*len(nums)
        i = len(nums)-1
        while i >= 0:
            min_val = min(nums[i], min_val)
            suffixMin[i] = min_val
            i -=1
        
        i= 0
        for i in range(0, len(nums)):
            max_val = max(max_val, nums[i])
            instab = max_val - suffixMin[i]
            if instab <= k:
                return i
        
        return -1
