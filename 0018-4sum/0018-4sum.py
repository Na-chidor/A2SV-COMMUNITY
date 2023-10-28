class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:
                return

            if N == 2:
                left, right = 0, len(nums)-1
                while left < right:
                    if nums[left] + nums[right] == target:
                        results.append(result + [nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                    elif nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
            else:
                for i in range(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

        nums.sort()
        results = []
        findNsum(nums, target, 4, [], results)
        return results
