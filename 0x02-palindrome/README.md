# 0x02 Palindrome
Given an integer x, return true if x is a 
palindrome , and false otherwise.

## Solution

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My first intuiton for this problem is to transform the number to string and reverse it.
# Approach
<!-- Describe your approach to solving the problem. -->
1. Transform the number to string
2. Reverse the string
3. Compare the reversed string with the original number
4. In order to gain more flexibility, outlie some special cases: when number is negative we cannot have a palindrome, so return false, and if the number is less than 10, the digit is the palindrome

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
    O(n)
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
    O(1)
# Code
```
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        x = str(x)
        return x == x[::-1]
```