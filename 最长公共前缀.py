# -*- coding: utf-8 -*-
# @Time    : 2018/9/19 09:28
# @Author  : zqj
# @FileName: 最长公共前缀.py
# @Software: PyCharm Community Edition
# @email   ：zihe@yscredit.com

'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
'''
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        elif len(strs) == 0:
            return ''
        else:
            a = []
            a.append(strs[0])
            for i in range(1,len(strs)):
                a.append(strs[i])
                c = min(len(a[0]),len(a[1]))
                if c == 0:
                    return ''
                else:
                    for i in range(c+1):
                        if a[0][:i] == a[1][:i]:
                            b = a[0][:i]
                            continue
                        else:
                            break
                a = [b]
            return b