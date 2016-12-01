#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
of rows like this: (you may want to display this pattern in a fixed font
for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and
make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""


class Solution(object):

    def convert(self, zig, numRows):

        #  count num by row and reached out to numRows then reverse

        n = len(zig)
        if numRows >= n or numRows <= 1:
            return zig

        zag = [''] * numRows
        row = 0
        step = 1
        for i in range(n):
            if row == 0:
                step = 1
            if row == numRows - 1:
                step = -1
            zag[row] += zig[i]
            # print(zag[row])
            row += step
        return "".join(zag)


if __name__ == "__main__":

    e = Solution()
    if e.convert('PAYPALISHIRING', 3) != "PAHNAPLSIIGYIR":
        raise("Not Passed!")
    else:
        print("Passed for example: PAYPALISHIRING with Row 3")
