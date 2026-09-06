class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        half = n//2
        ans = 0

        doubled = nums + nums
        prefix = [0] * (2*n+1)
        for i in range(2*n):
            prefix[i+1] = prefix[i] + doubled[i]

        for j in range(n):
            left = prefix[j+half] - prefix[j]
            right = prefix[j+n] - prefix[j+half]
            if left > right:
                ans +=1

        return ans