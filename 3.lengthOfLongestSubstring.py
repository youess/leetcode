#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import doctest


def lengthOfLongestSubstring(s):

    """
    type: s string
    rtype: int
    s[j] have a duplicate in the range of [i, j) with index j', we could replace
    just replace i with j' + 1 to find a new no repeat substring.
    >>> lengthOfLongestSubstring("b")
    1
    >>> lengthOfLongestSubstring("bbb")
    1
    >>> lengthOfLongestSubstring("abcabca")
    3
    >>> lengthOfLongestSubstring("abc")
    3
    >>> lengthOfLongestSubstring("dvdc")
    3
    """

    # extended ascii character number 256
    chr_map = [-1] * 256
    li = 0                # left index
    n = len(s)
    max_len = 0
    for ri in range(n):
        li = max(chr_map[ord(s[ri])], li)
        max_len = max(max_len, ri - li + 1)
        chr_map[ord(s[ri])] = ri + 1

    return max_len


doctest.testmod()
