class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []

        def flip(k):
            nonlocal arr
            arr[:k] = arr[:k][::-1]
            result.append(k)

        n = len(arr)
        for target in range(n, 1, -1):
            index = arr.index(target)
            if index == target - 1:
                continue
            if index != 0:
                flip(index + 1)
            flip(target)
        
        return result