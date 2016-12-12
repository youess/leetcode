#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Description:
Determine whether an integer is a palindrome. Do this without extra space.
"""


import doctest


class Solution:

    def isPalindrome(self, x):
        """
        Negative number is not counted as a palindrom number
        >>> e = Solution()
        >>> e.isPalindrome(121)
        True
        >>> e.isPalindrome(1231)
        False
        >>> e.isPalindrome(-121)
        False
        """
        return True if str(x) == str(x)[::-1] else False

    def reverse_int(self, x):
        ret = 0
        xx = abs(x)
        while xx:
            ret = ret * 10 + xx % 10
            xx //= 10
        if ret > 2147483647 or ret < -2147483648:
            ret = 0
        return -ret if x < 0 else ret

    def isPalindrome2(self, x):
        """
        Negative number is not counted as a palindrom number
        >>> e = Solution()
        >>> e.isPalindrome2(121)
        True
        >>> e.isPalindrome2(1231)
        False
        >>> e.isPalindrome2(-121)
        False
        """
        return True if x >= 0 and x == self.reverse_int(x) else False


if __name__ == "__main__":

    doctest.testmod()
