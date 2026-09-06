class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        cnt = 0
        for i in range(1, n+1):
            rotated = s[i:]+s[:i]
            score = 0
            for j in range(n-1):
                if rotated[j] == rotated[j+1]:
                    score+=1
            if score == k:
                cnt+=1
        return cnt