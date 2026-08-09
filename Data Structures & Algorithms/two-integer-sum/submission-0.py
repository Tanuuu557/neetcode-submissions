class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums [j] == target and i != j:
                    return [i,j]
nums= [3, 4, 5, 6]
target = 7
sol = Solution()
print(sol.twoSum(nums, target))