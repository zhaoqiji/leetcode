# -*- coding: utf-8 -*-
# @Time    : 2018/9/23 13:30
# @Author  : zqj
# @FileName: Z字形变换.py
# @Software: PyCharm Community Edition
# @email   ：zihe@yscredit.com

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        '''
        超时
        n = len(s)
        m = 2*numRows -2
        if m == 0:
            return s
        for i in range(numRows):
            exec('a_list{} = ""'.format(i))
        for i in range(n):
            a = i%m
            try:
                exec('a_list{} += "{}"'.format(a,s[i]))
            except:
                exec('a_list{} += "{}"'.format(m - a,s[i]))
        result = []
        for i in range(numRows):
            exec('result.append(a_list{})'.format(i))
        return ''.join(result)
        '''
        if numRows == 1:
            return s
        result_list = [''] * min(numRows,len(s))
        index = 0
        godown = False
        for each in s:
            result_list[index] += each
            if index == 0 or index == numRows-1:
                godown = not godown
            if godown:
                index += 1
            else :
                index -= 1
        return ''.join(result_list)
    