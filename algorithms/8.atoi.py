#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Description:

    Convert string into integer

"""


import doctest


class Solution:

    def myAtoi(self, s):
        """
        >>> e = Solution()
        >>> e.myAtoi("101")
        101
        >>> e.myAtoi("      101   ")
        101
        >>> e.myAtoi("      -00012a42   ")
        -12
        >>> e.myAtoi("+101")
        101
        >>> e.myAtoi("-101")
        -101
        >>> e.myAtoi("-242j1")
        -242
        >>> e.myAtoi("300000000000000000000")
        2147483647
        """

        if s == '':
            return 0

        n = 0
        i = 0
        s = list(s.strip())
        while s:
            c = ord(s.pop()) - 48
            if c >= 0 and c <= 9:
                n += 10**i * c
            elif c == -3 and s == []:
                n = -n
            elif c == -5 and s == []:
                pass
            else:
                # Got no num chars, remove previous numbers and re-calculate
                n = 0
                i = -1
            i += 1
        if n > 2147483647:
            return 2147483647
        elif n < -2147483648:
            return -2147483648
        else:
            return n

if __name__ == "__main__":

    doctest.testmod()
