# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 22:57
# @Author  : zqj
# @FileName: 反转整数.py
# @Software: PyCharm Community Edition
# @email   ：zihe@yscredit.com

'''
给定一个 32 位有符号整数，将整数中的数字进行反转。
示例 1:
输入: 123
输出: 321
示例 2:
输入: -123
输出: -321
示例 3:
输入: 120
输出: 21
注意:
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。
根据这个假设，如果反转后的整数溢出，则返回 0。
'''
import math
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = ''
        if x > 0:
            for i in str(x)[::-1]:
                y = y + i

            y = int(y)
        else:
            x = -1 * x
            for i in str(x)[::-1]:
                y = y + i
            y = int(y) * -1
        if y in range(int(-1 * math.pow(2, 31)), int(math.pow(2, 31))):
            return y
        else:
            return 0