# -*- coding: utf-8 -*-
# @Time    : 2018/9/22 20:12
# @Author  : zqj
# @FileName: 两个排序数组的中位数.py
# @Software: PyCharm Community Edition
# @email   ：zihe@yscredit.com

'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。

请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。

你可以假设 nums1 和 nums2 不同时为空
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nusm = sorted(nums1+nums2)
        if len(nusm) % 2 == 1:
            a = int((len(nusm) - 1)/2)
            return nusm[a]
        else:
            a = int(len(nusm)/2)
            b = int(len(nusm)/2 - 1)
            return (nusm[a] + nusm[b])/2