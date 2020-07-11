class Solution:
    def permute(self, nums):
        res = []
        def backtrack(nums,tmp_list):
            res.append(tmp_list)
            for i in range(len(tmp_list)):
                backtrack(nums[:i]+nums[i+1:],tmp_list+nums[i])
        backtrack(nums,[])
        return res

