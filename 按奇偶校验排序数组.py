# -*- coding: utf-8 -*-
# @Time    : 2018/9/19 15:27
# @Author  : zqj
# @FileName: 按奇偶校验排序数组.py
# @Software: PyCharm Community Edition
# @email   ：zihe@yscredit.com

'''
给定一个非负整数数组 A，返回一个由 A 的所有偶数元素组成的数组，后面跟 A 的所有奇数元素。

你可以返回满足此条件的任何数组作为答案。
'''
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        a = [x for x in A if x%2 == 0]
        b = [x for x in A if x%2 == 1]
        return a+b