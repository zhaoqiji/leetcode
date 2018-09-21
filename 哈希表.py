# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 20:49
# @Author  : zqj
# @FileName: 哈希表.py
# @Software: PyCharm Community Edition
# @email   ：zihe@yscredit.com

'''
使用哈希表可以非常快速的进行查找操作
查找时间为常数，不需要元素有序排序
python 的内建函数字典就是用哈希表实现的
'''

#1.一种简单的实现方法：
class Linermap(object):
    def __init__(self):
        self.items = []
    #往表里添加元素
    def add(self,k,v):
        self.items.append((k,v))
    #线性方式查找元素
    def get(self,k):
        for key,value in self.items:
            if key == k:
                return value
        raise KeyError

'''
我们可以在使用add添加元素时让items列表保持有序,而在使用get时使用二分法查找，
此时时间复杂度为O(logn)
而往列表中插入一个新元素实际上是一个线性操作，所以这不是最好的方法
'''

#2 改进版本
'''
将总查询表分割为若干个较小的子段，比如100个子段
通过hash函数求出某个建的哈希值,再通过计算，得到往哪个子段中进行添加或者查找
所以相对于从头开始搜索列表，时间会极大的缩短
'''

#hash 函数用于获取一个字符串或者数值的hash值，这是一个唯一的一个值,返回int
class BetterMap(object):
    #利用linear_map作为子表，建立更快的查询表
    def __init__(self,n):
        self.maps = []
        #n 表示要构建的子表的个数
        for i in range(n):
            self.maps.append(Linermap())
    #通过hash函数计算索引值
    def find_map(self,k):
        #取余数放入，或者查找
        index = hash(k) % len(self.maps)
        #返回索引表的引用
        return self.maps[index]
    #寻找合适的子表(LineraMap对象)进行添加或者查找
    def add(self,k,v):
        m = self.find_map(k) #这是一个LinearMap 对象
        m.add(k,v) #调用LinearMap对象里面的add方法进行添加
    def get(self,k):
        m = self.find_map(k)
        m.get(k)
#当n=100时， BetterMap的查找速度大约是LinearMap的100倍

'''
Hashtable 的实现
'''
class Hashtable(object):
    def __init__(self):
        #初始化总表数为，容量为2的表格(含两个子表)
        self.hs_map = BetterMap(2)
        self.num = 0 #初始的表中的数据个数
    def get(self,k):
        return self.hs_map.get(k)
    def add(self,k,v):
        #若当前元素数量达到临界值(子总表数)时，进行重排列
        #对总表进行扩张，增加子表个数为当前元素个数的两倍
        if self.num == len(self.hs_map.maps):
            self.resize()
        #往重排之后的self.ha_map中添加新的元素
        self.hs_map.add(k,v)
        self.num += 1
    def resize(self):
        #进行重排操作，添加新表，注意重排需要线性时间
        #先新建一个新表，子表数等于两倍的元素个数
        new_maps = BetterMap(2 * self.num)
        for m in self.hs_map.maps:
            for k,v in m.items():
                new_maps.add(k,v)

'''
初始情况为只有2个linear_map 的better_map
[[linear_map],[linear_map]]
即self.ha_map.map == [linear_map],[linear_map],长度为2
0 < 2,掉用better_map 中的add(k,v)方法。
add(k,v)方法首先通过hash函数和find_map方法找到所对应的linear_map
在所对应的linear_map中append(k,v)
假设我们要添加32个元素，过程如下：
1. 由于初始长度为2，前两次add不需要重排，第1,2次 总时间为 2
2. 第3次add，重排为4，耗时2，第3次时间为 3
3. 第4次add，耗时1　　　　到目前为止，总时间为 6
4. 第5次add，重排为 8，耗时4，第5次时间为5
5. 第6~8次   共耗时3    　　到目前为止，总时间为 6+5+3 = 14
6. 第9次add，重排16，  耗时8，第9次时间为9
7. 第10~16次，共耗时7，　到目前为止，总时间为 14+9+7 = 30
在32次add后，总时间为62的单位时间，由以上过程可以发现一个规律，在n个元素add之后，
当n为2的幂，则当前总单位时间为 2n-2，所以平均add时间绝对小于2单位时间。
当n为2的幂时，为最合适的数量，当n变大之后，平均时间为稍微上升，但重要的是，我们达到了O(1)。
'''









