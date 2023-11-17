#!/usr/bin/python3
"""palindrome module"""


def isPalindrome(self, x: int) -> bool:
    """isPalindrome function verifies if a number is a palindrome or not
    Returns: True or False
    """
    if x < 0:
        return False
    if x < 10:
        return True
    x = str(x)
    return x == x[::-1]