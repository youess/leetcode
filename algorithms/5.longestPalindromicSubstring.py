#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):

    def longestPalindromicSubstring_dp(self, s):

        """
        dynamic programming, longest palindromic substring can be broken into
        two parts, time: O(n^2), space: O(n^2)
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

    def longestPalindromicSubstring_center(self, s):
        """
        Center by one element and calulate each palindromic substring by
        expanding the letters
        """
        ls = len(s)
        if ls == 1:
            return s

        maxLen, start = (0, 0)
        for i in range(1, ls):
            #  center as i, expanding as even palindrom
            low, high = (i - 1, i)
            while low >= 0 and high < ls and s[low] == s[high]:
                low -= 1
                high += 1
            if high - low - 1 > maxLen:
                maxLen = high - low - 1
                start = low + 1

            low, high = (i - 1, i + 1)
            #  center as i, expanding as odd palindrom
            while low >= 0 and high < ls and s[low] == s[high]:
                low -= 1
                high += 1
            if high - low - 1 > maxLen:
                maxLen = high - low - 1
                start = low + 1

        return s[start:(maxLen+start)]

    def longestPalindromicSubstring_manacher(self, s):
        pass


if __name__ == "__main__":

    e = Solution()
    #  print(e.longestPalindromicSubstring_dp("babad"))      # bab or aba
    #  print(e.longestPalindromicSubstring_dp("cbbd"))       # bb
    #  print(e.longestPalindromicSubstring_dp("abcda"))      # a

    #  print(e.longestPalindromicSubstring_center("babad"))
    #  print(e.longestPalindromicSubstring_center("cbbd"))
    #  print(e.longestPalindromicSubstring_center("abcda"))
