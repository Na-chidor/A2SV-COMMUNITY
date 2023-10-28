class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        n=len(s)
        longest=0
        my_set=set()
        while j<n:
            if s[j] not in my_set:
                my_set.add(s[j])
                j+=1
                longest=max(longest,j-i)
            elif s[j] in my_set:
                my_set.remove(s[i])
                i+=1
        return longest