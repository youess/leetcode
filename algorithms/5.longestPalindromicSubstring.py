#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):

    def longestPalindromicSubstring_dp(self, s):

        """
        dynamic programming, longest palindromic substring can be broken into
        two parts
        1) i == j, true
        2) i != j, m[i+1][j-1] = s[i] == s[j] and m[i+1][j-1]
        """

        n = len(s)
        #  initilize the python 2-d array
        #  m = [[0] * n] * n, wrong!
        m = [x[:] for x in [[0] * n] * n]
        longest_str = ""
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j or (s[i] == s[j] and
                              (j - i < 2 or m[i+1][j-1] == 1)):
                    m[i][j] = 1
                    #  print("{0}, {1}".format(i, j))
                    # if j - i >= 2:
                    #    print(m[i+1][j-1])
                    if len(longest_str) < (j - i + 1):
                        longest_str = s[i:(j+1)]

        return longest_str

    def longestPalindromicSubstring_manacher(self, s):
        pass


if __name__ == "__main__":

    e = Solution()
    #  print(e.longestPalindromicSubstring_dp("babad"))
    #  print(e.longestPalindromicSubstring_dp("cbbd"))
    #  print(e.longestPalindromicSubstring_dp("abcda"))
