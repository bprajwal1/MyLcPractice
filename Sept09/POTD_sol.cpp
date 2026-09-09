class Solution {
public:
    long long countCommas(long long n) {
       long long p = 1000;
       long long ans = 0;
       while(p<=n){
        ans += n - p + 1;
        p *= 1000;
       }
       return ans;
    }
};