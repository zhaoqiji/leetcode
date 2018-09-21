# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 23:23
# @Author  : zqj
# @FileName: 罗马数字转整数.py
# @Software: PyCharm Community Edition
# @email   ：zihe@yscredit.com

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = ['M','D','C','L','X','V','I']
        sm = 0
        for i in range(len(a)):
            s = s.replace(a[i],str(7-i))
        num_dict = {
            '7' : 1000,
            '6' : 500,
            '5' : 100,
            '4' : 50,
            '3' : 10,
            '2' : 5,
            '1' : 1
        }
        for j in range(len(s)-1):
            if int(s[j]) >= int(s[j+1]):
                sm += num_dict.get(s[j],0)
            else:
                sm -= num_dict.get(s[j],0)
        sm += num_dict.get(s[-1],0)
        return sm
