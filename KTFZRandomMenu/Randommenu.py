#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：小工具
@File ：Randommenu.py
@IDE  ：PyCharm
@Author ：xiguazhale
@Date ：2021/9/26 19:27
'''
import random  # 引入随机库
import time


def Blanklines():  # 打印一行空白行，定义一个函数
	print()


def Waiting():
	time.sleep(1)


input("请按回车键，进行菜单随机选取，祝你好运。")
Blanklines()

scale = 50
print("选取开始，纠结中".center(scale // 2, "-"))
start = time.perf_counter()
for i in range(scale + 1):
	a = "*" * i
	b = "." * (scale - i)
	c = (i / scale) * 100
	dur = time.perf_counter() - start
	print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
	time.sleep(0.1)
print("\n" + "选取结束，猜猜看".center(scale // 2, "-"))

print("揭晓中...")
Waiting()
print(3)
Waiting()
print(2)
Waiting()
print(1)
Waiting()
Blanklines()

menus = ['广式火锅', '老北京涮羊肉火锅', '牛肉火锅', '羊血火锅', '羊蝎子火锅', '烤鸭', '自助烧烤', '羊肉', '猪肚鸡', '面', '寿司', '寿喜锅', '日餐', '自助餐', '汤包',
		 '锅贴', '串串火锅', '湘菜', '川菜', '东北铁锅炖', '早茶', '椰子鸡', '淮扬菜', '越南菜', '米线', '臊子面', '牛排', '西餐', '披萨', '炸鸡', '汉堡',
		 '肉蟹煲', '麻食', '烤肉', '菠菜面', '泡馍', '日式拉面', '螺蛳粉', '牛肉拉面', '延安沾沾', '葫芦鸡', '麻辣烫', '黄焖鸡', '钵钵鸡', '小龙虾', '新疆炒米粉',
		 '鱼火锅', '酸菜鱼', '烤鱼', '云南菜', '俄罗斯菜', '烤牛肉', '焖锅', '烤生蚝', '鲁菜', '泰国菜', '韩式部队锅', '手抓羊肉'
	, '徽菜牛蛙', '重庆纸包鱼', '陕菜']  # 定义列表这里存放你要点名同学的名字
menu = random.choice(menus)
print("别纠结了，也别想了，今天我们就吃这个吧！！----", menu)
Blanklines()
input("请再次按回车键以关闭窗口，我们下次再见。")
