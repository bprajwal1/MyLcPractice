class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        positions = defaultdict(list)
        
        for id, num in enumerate(nums):
            positions[num].append(id)
        ans = 0

        for num, ind in positions.items():
            if len(ind) == 3:
                if ind[1] - ind[0] == ind[2] - ind[1]:
                    ans += 1
        return ans
            