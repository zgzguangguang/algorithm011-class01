'''
移动零
'''

class Solution:
    def movezero(self,nums):
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            elif count > 0:
                nums[i-count],nums[i] = nums[i],0
        return nums
    def movezero2(self,nums):
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[index] = nums[index],nums[i]
                index += 1
        return nums