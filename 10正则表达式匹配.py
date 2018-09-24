# -*- coding: utf-8 -*-
# @Time    : 2018/9/24 10:14
# @Author  : zqj
# @FileName: 10正则表达式匹配.py
# @Software: PyCharm Community Edition
# @email   ：zihe@yscredit.com
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        for i in range(len(p)):
            if p[i] == '*':
                pass
            else:
                p = p[i:]
                break
        try:
            a = re.compile(p).findall(s)[0]
            if len(a) == len(s):
                return True
            else :
                return False
        except:
            return False