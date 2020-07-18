class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums==[]:
            return -1
        l=0
        r=len(nums)-1
        while l<r:
            mid=l+(r-l)//2
            if nums[mid]<nums[r]:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid
            else:
                if nums[l]<=target<=nums[mid]:
                    r=mid
                else:
                    l=mid+1
        if nums[l]==target:
            return l
        else:
            return -1



class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        max_dst = 1
        while i < max_dst:
            max_dst = max(max_dst,i+nums[i]+1)
            if max_dst >= len(nums):
                return True
            i += 1
        return False