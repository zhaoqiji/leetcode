# -*- coding: utf-8 -*-
# @Time    : 2018/9/19 10:06
# @Author  : zqj
# @FileName: 有效的括号.py
# @Software: PyCharm Community Edition
# @email   ：zihe@yscredit.com
'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，
判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
'''
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = ['(', '[', '{']
        a_dict = {')': '(', ']': '[', '}': '{'}
        b = []
        for i in s:
            if i in a:
                b.append(i)
            else:
                if len(b) == 0:
                    return False
                else:
                    if b[-1] == a_dict[i]:
                        b.pop()
                    else:
                        return False
        if b == []:
            return True
        else:
            return False