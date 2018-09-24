# -*- coding: utf-8 -*-
# @Time    : 2018/9/24 17:18
# @Author  : zqj
# @FileName: 12整数转罗马数字.py
# @Software: PyCharm Community Edition
# @email   ：zihe@yscredit.com
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        a = ''
        a_dict = {
            '1' : 'I',
            '5' : 'V',
            '10' : 'X',
            '50' : 'L',
            '100' : 'C',
            '500' : 'D',
            '1000' : 'M' ,
        }
        num = str(num)[::-1]
        for i in range(len(num)):
            if int(num[i]) == 0:
                pass
            elif 1 <= int(num[i]) <=3:
                a = a_dict.get(str(10**i),'') * int(num[i]) + a
            elif int(num[i]) == 4:
                a = a_dict.get(str(10**i),'') + a_dict.get(str(5 * 10**i),'') + a
            elif int(num[i]) == 5:
                a = a_dict.get(str(5 * 10**i),'') + a
            elif 6 <= int(num[i]) <= 8:
                print(a,1)
                a = a_dict.get(str(5 * 10**i),'') + a_dict.get(str(10**i),'') * (int(num[i]) - 5) + a
                print(a,2)
            else :
                a = a_dict.get(str(10**i),'') + a_dict.get(str(10**(i+1)),'') + a
        return a