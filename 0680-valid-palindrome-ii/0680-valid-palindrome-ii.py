class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Try deleting either the character at left or right
                return is_palindrome(left, right - 1) or is_palindrome(left + 1, right)
            left += 1
            right -= 1
        
        # The string is already a palindrome or can be made a palindrome
        return True