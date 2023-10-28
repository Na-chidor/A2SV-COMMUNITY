class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prev_window = sum(nums[:k])
        max_ave = prev_window
        for i in range(n - k):
            prev_window = prev_window + nums[k+i] - nums[i]
            max_ave = max(max_ave, prev_window)
        return max_ave / k



        
