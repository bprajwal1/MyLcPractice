class Solution:
    def countCommas(self, n: int) -> int:
        cnt = 0
        for i in range(1, n+1):
            if len(str(i))>3:
                cnt +=1
        return cnt