class Solution:
    def calculateSum(self, num: int) -> int:
        sum = 0
        while num > 0:
            sum  += num%10
            num //= 10
        return sum
    
    
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if (self.calculateSum(nums[i]) == i):
                return i 
        
        return -1