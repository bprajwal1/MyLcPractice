class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i in range(0, len(s)): 
            ans += (i + 1) *(ord('z') - ord(s[i]) + 1)
        return ans