# -*- coding: utf-8 -*-
# @Time    : 2018/9/22 20:30
# @Author  : zqj
# @FileName: 5最长回文串.py
# @Software: PyCharm Community Edition
# @email   ：zihe@yscredit.com
'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
'''
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s),-1,-1):
            for j in range(len(s)-i+1):
                a = s[j:j+i]
                if a == a[::-1]:
                    return a