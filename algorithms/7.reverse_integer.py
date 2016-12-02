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
        pass


if __name__ == "__main__":

    doctest.testmod()
