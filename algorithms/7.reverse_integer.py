"""
Description:

"""


import doctest


class Solution:

    def reverse(self, x):

        """
        >>> e = Solution()
        >>> e.reverse(321)
        123
        >>> e.reverse(-321)
        -123
        >>> e.reverse(1000000003)
        0
        """
        xx = int(str(abs(x))[::-1])
        # integer overflow
        if xx > 2147483648:
            return 0
        return xx if x > 0 else -xx

    def reverse_integer(self, x):
        """
        >>> e = Solution()
        >>> e.reverse_integer(321)
        123
        >>> e.reverse_integer(-321)
        -123
        >>> e.reverse_integer(1000000003)
        0
        """
        if x == 0:
            return 0
        ret = 0
        flag = 1 if x < 0 else 0
        x = abs(x)
        while x:
            ret = ret * 10 + x % 10
            x //= 10
        if ret > 2147483647 or ret < -2147483648:
            ret = 0
        return -ret if flag else ret


if __name__ == "__main__":

    doctest.testmod()
