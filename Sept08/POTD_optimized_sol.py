'''Since numbers greater than 999 will contain atleast 1 comma, when we categorize 
 the ranges within 1000 to 10**5 we get n-999 as the total commas across the number range
'''
class Solution:
    def countCommas(self, n: int) -> int:
        return max(n-999, 0)