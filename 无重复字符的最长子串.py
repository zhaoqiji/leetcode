# -*- coding: utf-8 -*-
# @Time    : 2018/9/19 15:18
# @Author  : zqj
# @FileName: 无重复字符的最长子串.py
# @Software: PyCharm Community Edition
# @email   ：zihe@yscredit.com

'''
给定一个字符串，找出不含有重复字符的最长子串的长度。
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = []
        l_max = 0
        for i in s:
            if i not in a:
                a.append(i)
            else:
                l = len(a)
                if l > l_max:
                    l_max = l
                c = a.index(i)
                a = a[c + 1:]
                a.append(i)
        return max(len(a), l_max)
