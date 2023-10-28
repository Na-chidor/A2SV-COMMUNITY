class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        longest = 0
        char_set = set()

        while j < len(s):
            if s[j] not in char_set:
                char_set.add(s[j])
                j += 1
                longest = max(longest, j - i)
            else:
                char_set.remove(s[i])
                i += 1

        return longest

            
            