#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys


text = '''"""
Description:

"""


import doctest


class Solution:

    def function(self):
        """
        >>> e = Solution()
        """
        pass


if __name__ == "__main__":

    doctest.testmod()
'''

with open(sys.argv[1], 'w') as f:
    f.write(text)
