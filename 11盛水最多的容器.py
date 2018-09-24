# -*- coding: utf-8 -*-
# @Time    : 2018/9/24 16:36
# @Author  : zqj
# @FileName: 11盛水最多的容器.py
# @Software: PyCharm Community Edition
# @email   ：zihe@yscredit.com

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        超时
        if len(height) <= 1:
            return 0
        s = 0
        for i in range(len(height)-1):
            for j in range(i+1,len(height)):
                ss = (j-i) * min(height[i],height[j])
                s = max(ss,s)
        return s
        '''
        """
        逼近,每次左右两端都舍去短的那一端
        """
        left = 0
        right = len(height) - 1
        s = 0
        if len(height) <= 1:
            return 0
        for i in range(len(height)-1):
            ss = (right - left) * min(height[right],height[left])
            s = max(s,ss)
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return s