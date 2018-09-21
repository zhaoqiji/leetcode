# -*- coding: utf-8 -*-
# @Time    : 2018/9/19 15:31
# @Author  : zqj
# @FileName: 汉明距离.py
# @Software: PyCharm Community Edition
# @email   ：zihe@yscredit.com
'''
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。
'''

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a = bin(x)[2:]
        b = bin(y)[2:]
        if len(a) < len(b):
            c = a
            a = b
            b = c
        d = len(a) - len(b)
        b = '0' * d + b
        sm = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                sm += 1
        return sm