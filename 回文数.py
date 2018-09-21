# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 23:17
# @Author  : zqj
# @FileName: 回文数.py
# @Software: PyCharm Community Edition
# @email   ：zihe@yscredit.com

'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
'''
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            a = ''
            for i in str(x)[::-1]:
                a = a + i
            a = int(a)
            if a == x:
                return True
            else :
                return False