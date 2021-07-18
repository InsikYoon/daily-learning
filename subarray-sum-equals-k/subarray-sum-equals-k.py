class Solution(object):
    
    def update_table(self, sum_table, prev_sum):
        if prev_sum in sum_table.keys():
            sum_table[prev_sum] = sum_table[prev_sum]+1
        else:
            sum_table[prev_sum] = 1
    
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_table ={0:1}
        prev_sum = 0   
        out = 0
        prefix_sum = []
        
        
        prev_sum = 0
        for i in range(len(nums)):
            prev_sum += nums[i]
            if prev_sum-k in sum_table:
                out += sum_table[prev_sum-k]
            sum_table[prev_sum] = sum_table.get(prev_sum,0)+1
        return out