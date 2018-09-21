# -*- coding: utf-8 -*-
# @Time    : 2018/9/21 09:50
# @Author  : zqj
# @FileName: 2两数相加.py
# @Software: PyCharm Community Edition
# @email   ：zihe@yscredit.com

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = []
        b = []
        while l1:
            a.append(l1.val)
            l1 = l1.next

        while l2:
            b.append(l2.val)
            l2 = l2.next
        if len(a) == len(b):
            pass
        elif len(a) < len(b):
            for i in range(len(b) - len(a)):
                a.append(0)
        else:
            for i in range(len(a) - len(b)):
                b.append(0)
        a = a[::-1]
        b = b[::-1]
        c = [x + y for x, y in zip(a, b)]
        sm = 0
        for i in range(len(c) - 1, -1, -1):
            sm += c[len(c) - i - 1] * 10 ** i
        res = []
        for x in str(sm):
            res.append(int(x))
        res = res[::-1]
        return res

