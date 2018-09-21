# -*- coding: utf-8 -*-
# @Time    : 2018/9/19 15:52
# @Author  : zqj
# @FileName: 下一个更大元素.py
# @Software: PyCharm Community Edition
# @email   ：zihe@yscredit.com

'''
给定两个没有重复元素的数组 nums1 和 nums2 ，
其中nums1 是 nums2 的子集。
找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
nums1 中数字 x 的下一个更大元素是指 x 在 nums2
中对应位置的右边的第一个比 x 大的元素。
如果不存在，对应位置输出-1。


'''


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for x in nums1:
            a = nums2.index(x)
            if a == len(nums2) - 1:
                result.append(-1)
            else:
                if x >= max(nums2[a + 1:]):
                    result.append(-1)
                    continue
                else:
                    for y in nums2[a + 1:]:
                        if y > x:
                            result.append(y)
                            break
        return result
