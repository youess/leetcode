#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):

        def findKth(a, m, b, n, k):

            #  always assume m < n
            if m > n:
                return findKth(b, n, a, m, k)
            #  consider null arrary
            if m == 0:
                return b[k-1]
            #  when k is 1
            if k == 1:
                return min(a[0], b[0])

            #  find k/2 number on each arrarys
            pa = min(k // 2, m)
            pb = k - pa
            if a[pa-1] < b[pb-1]:
                return findKth(a[pa:], m-pa, b, n, k-pa)
            elif a[pa-1] > b[pb-1]:
                return findKth(a, m, b[pb:], n-pb, k-pb)
            else:
                return a[pa-1]

        m = len(nums1)
        n = len(nums2)
        total = m + n
        #  print("{0}\t{1}\t{2}".format(m, n, total))
        if total % 2 == 0:
            return (findKth(nums1, m, nums2, n, total // 2) +
                    findKth(nums1, m, nums2, n, total // 2 + 1)) / 2.0
        else:
            return findKth(nums1, m, nums2, n, total // 2 + 1)

if __name__ == "__main__":
    e = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    print(e.findMedianSortedArrays(nums1, nums2))
    nums1 = [2]
    nums2 = []
    print(e.findMedianSortedArrays(nums1, nums2))
    nums1 = [1, 3]
    nums2 = [2, 4]
    print(e.findMedianSortedArrays(nums1, nums2))
