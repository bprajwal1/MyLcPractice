class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        positions = defaultdict(list)
        
        for id, num in enumerate(nums):
            positions[num].append(id)
        ans = 0

        for num, ind in positions.items():
            if len(ind) >= 3:
                diff = ind[1] - ind[0]
                ok = True
                for i in range(2, len(ind)):
                    if ind[i] - ind[i-1] != diff:
                        ok = False
                        break
                if ok:
                    ans += 1
        return ans
                