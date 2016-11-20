#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a string, find the length of the longest substring without
repeating characters. Note that substring is not subsequence.
"""


import doctest


def lengthOfLongestString(s):
    """
    :type s: str
    :rtype: int
    >>> lengthOfLongestString("pwwkew")
    3
    >>> lengthOfLongestString("abc")
    3
    >>> lengthOfLongestString("")
    0
    >>> lengthOfLongestString("dvdf")
    3
    """
    CHAR_NUM = 256
    char_map = [-1] * CHAR_NUM
    n = len(s)
    max_len = 0
    left = 0
    for i in range(n):
        left = char_map[s[i]]
        if left != -1:
            max_len = max(i - left, max_len)

doctest.testmod()
