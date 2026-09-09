'''
Time complexity-> O(logn).

The loop runs O(log1000 n) times because p is multiplied by 1000 in each iteration (at most 5 iterations for n≤10 
15).

Space complexity-> O(1).
'''

class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        p = 1000
        while p<=n:
            ans += n - p + 1
            p *= 1000
        return ans