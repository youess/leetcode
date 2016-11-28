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

    def longestPalindromicSubstring_opt_center(self, s):
        """
        Center by one element and calulate each palindromic substring by
        expanding the letters
        """
        ls = len(s)
        if ls == 1:
            return s

        start, end = (0, 0)

        def expand_around_center(s, low, high):

            while low >= 0 and high < ls and s[low] == s[high]:
                low -= 1
                high += 1
            return high - low - 1

        for i in range(1, ls):
            len1 = expand_around_center(s, i, i)
            len2 = expand_around_center(s, i, i+1)
            ml = max(len1, len2)
            if ml > end - start:
                start = i - (ml - 1) // 2
                end = i + ml // 2
        return s[start:end+1]

    def longestPalindromicSubstring_manacher(self, s):
        #  refer to http://www.cnblogs.com/TenosDoIt/p/3675788.html
        #  idx as current longest palindrom string center
        #  mx as current longest palindrom string most right position
        def pre_process(s):
            rs = '^'
            for se in s:
                rs += '#' + se
            rs += '#$'
            return rs

        if len(s) == 1:
            return s
        ss = pre_process(s)
        ls, idx, mx = (len(ss), 0, 0)

        print("'" + ', '.join(list(ss)) + "'")
        # initilize the point array
        p = [0] * ls
        for i in range(1, ls-1):
            p[i] = min(p[2*idx-i], p[mx-i]) if mx > i else 1
            print(p)
            while ss[i+p[i]] == ss[i-p[i]]:
                p[i] += 1
            if i + p[i] > mx:
                mx = i + p[i]
                idx = i

        maxLen, index = (0, 0)
        for i in range(1, ls-1):
            if p[i] > maxLen:
                maxLen = p[i]
                index = i

        #  print("{0}, {1}".format(maxLen, index))
        start = (index - maxLen) // 2
        end = start + maxLen - 1
        return s[start:end]


if __name__ == "__main__":

    e = Solution()
    #  print(e.longestPalindromicSubstring_dp("babad"))      # bab or aba
    #  print(e.longestPalindromicSubstring_dp("cbbd"))       # bb
    #  print(e.longestPalindromicSubstring_dp("abcda"))      # a

    #  print(e.longestPalindromicSubstring_center("babad"))
    #  print(e.longestPalindromicSubstring_center("cbbd"))
    #  print(e.longestPalindromicSubstring_center("abcda"))

    #  print(e.longestPalindromicSubstring_opt_center("babad"))
    #  print(e.longestPalindromicSubstring_opt_center("cbbd"))
    #  print(e.longestPalindromicSubstring_opt_center("abcda"))

    print(e.longestPalindromicSubstring_manacher("babad"))
    print(e.longestPalindromicSubstring_manacher("cbbd"))
    print(e.longestPalindromicSubstring_manacher("abcda"))
