class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        area0=0
        while i<j:
            area1=(j-i)*min(height[i],height[j])
            area0=max(area0,area1)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return area0
            
