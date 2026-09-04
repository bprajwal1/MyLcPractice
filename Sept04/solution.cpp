class Solution {
public:
    static int firstStableIndex(vector<int>& nums, int k) {
        int min_val = INT_MAX;
        int max_val = INT_MIN;
        vector<int> suffixMin(nums.size(), 0);
        int inst = 0;

        for(int i=nums.size()-1; i>=0; i--)
        {
            min_val = min(min_val, nums[i]);
            suffixMin[i] = min_val;
        }
        
        for(int i=0; i<nums.size(); i++)
        {
            max_val = max(max_val, nums[i]);
            inst = max_val - suffixMin[i];

            if (inst <= k)
            {
                return i;
            }
        }

        return -1;
    }
};