'''
删除排序数组中的重复项
'''


class Solution:
    def removeDuplicates(self,nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] !=  nums[j]:
                j += 1
                nums[j] = nums[i]
        return j+1
    def removeDuplicate2(self,nums):
        s_nums = set(nums)
        l_nums = list(s_nums)
        return len(l_nums)