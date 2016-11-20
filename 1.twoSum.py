#!/usr/bin/env python
# -*- coding: utf-8 -*-


import doctest


def twoSum(nums, target):
    """
    Return a list of index. Assume only have exactly one solution
    @nums list[int],
    @target int
    @rtype list[int]
    >>> twoSum([2, 7, 11, 15], 9)
    [0, 1]
    """
    m = dict()
    nLen = len(nums)
    for i in range(nLen):
        theOtherNum = target - nums[i]
        if theOtherNum in m:
            return [m[theOtherNum], i]
            #  return sorted([i, m[theOtherNum]])
        else:
            m[nums[i]] = i


doctest.testmod()
#  print(twoSum([1, 2, 3, 4, 5, 6], 6))
