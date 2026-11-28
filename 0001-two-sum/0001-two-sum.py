class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr =[]
        for j in range(len(nums)):
            for i in range(1,len(nums)):
                if i != j:
                    if nums[j] + nums[i] == target:
                        arr = [j,i]
                        return arr
        