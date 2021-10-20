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


# def randoms():  # 随机菜单
# 	menus = ['广式火锅', '老北京涮羊肉火锅', '牛肉火锅', '羊血火锅', '羊蝎子火锅', '烤鸭', '自助烧烤', '羊肉', '猪肚鸡', '面', '寿司', '寿喜锅', '日餐', '自助餐',
# 			 '汤包',
# 			 '锅贴', '串串火锅', '湘菜', '川菜', '东北铁锅炖', '早茶', '椰子鸡', '淮扬菜', '越南菜', '米线', '臊子面', '牛排', '西餐', '披萨', '炸鸡', '汉堡',
# 			 '肉蟹煲', '麻食', '烤肉', '菠菜面', '泡馍', '日式拉面', '螺蛳粉', '牛肉拉面', '延安沾沾', '葫芦鸡', '麻辣烫', '黄焖鸡', '钵钵鸡', '小龙虾', '新疆炒米粉',
# 			 '鱼火锅', '酸菜鱼', '烤鱼', '云南菜', '俄罗斯菜', '烤牛肉', '焖锅', '烤生蚝', '鲁菜', '泰国菜', '韩式部队锅', '手抓羊肉'
# 		, '徽菜牛蛙', '重庆纸包鱼', '陕菜']
# 	menu = random.choice(menus)
# 	print("请珍惜每一次的随机选择！！----", menu)


def select():  # 进度条
	scale = 50
	print("选取开始".center(scale // 2, "-"))
	start = time.perf_counter()
	for i in range(scale + 1):
		a = "*" * i
		b = "." * (scale - i)
		c = (i / scale) * 100
		dur = time.perf_counter() - start
		print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
		time.sleep(0.1)
	print("\n" + "选取结束，猜猜看".center(scale // 2, "-"))


input("每回合只有 三 次选择的机会,按回车键开始选择!!!")
Blanklines()

# -----------第一次选取-----------
input("请按回车键进行第1次菜单随机选取：")
select()
print("揭晓中...")
Waiting()
menus = ['广式火锅', '老北京涮羊肉火锅', '牛肉火锅', '羊血火锅', '羊蝎子火锅', '烤鸭', '自助烧烤', '羊肉', '猪肚鸡', '面', '寿司', '寿喜锅', '日餐', '自助餐',
		 '汤包',
		 '锅贴', '串串火锅', '湘菜', '川菜', '东北铁锅炖', '早茶', '椰子鸡', '淮扬菜', '越南菜', '米线', '臊子面', '牛排', '西餐', '披萨', '炸鸡', '汉堡',
		 '肉蟹煲', '麻食', '烤肉', '菠菜面', '泡馍', '日式拉面', '螺蛳粉', '牛肉拉面', '延安沾沾', '葫芦鸡', '麻辣烫', '黄焖鸡', '钵钵鸡', '小龙虾', '新疆炒米粉',
		 '鱼火锅', '酸菜鱼', '烤鱼', '云南菜', '俄罗斯菜', '烤牛肉', '焖锅', '烤生蚝', '鲁菜', '泰国菜', '韩式部队锅', '手抓羊肉'
	, '徽菜牛蛙', '重庆纸包鱼', '陕菜']
menu1 = random.choice(menus)
print("请珍惜每一次的随机选择！！----", menu1)
Blanklines()

# -----------第二次选取-----------
input("请按回车键进行第2次菜单随机选取：")
select()
print("揭晓中...")
Waiting()
menus = ['广式火锅', '老北京涮羊肉火锅', '牛肉火锅', '羊血火锅', '羊蝎子火锅', '烤鸭', '自助烧烤', '羊肉', '猪肚鸡', '面', '寿司', '寿喜锅', '日餐', '自助餐',
		 '汤包',
		 '锅贴', '串串火锅', '湘菜', '川菜', '东北铁锅炖', '早茶', '椰子鸡', '淮扬菜', '越南菜', '米线', '臊子面', '牛排', '西餐', '披萨', '炸鸡', '汉堡',
		 '肉蟹煲', '麻食', '烤肉', '菠菜面', '泡馍', '日式拉面', '螺蛳粉', '牛肉拉面', '延安沾沾', '葫芦鸡', '麻辣烫', '黄焖鸡', '钵钵鸡', '小龙虾', '新疆炒米粉',
		 '鱼火锅', '酸菜鱼', '烤鱼', '云南菜', '俄罗斯菜', '烤牛肉', '焖锅', '烤生蚝', '鲁菜', '泰国菜', '韩式部队锅', '手抓羊肉'
	, '徽菜牛蛙', '重庆纸包鱼', '陕菜']
menu2 = random.choice(menus)
print("请珍惜每一次的随机选择！！----", menu2)
Blanklines()

# -----------第三次选取-----------
input("请再次按回车键进行第3次菜单随机选取：")
select()
print("揭晓中...")
Waiting()
menus = ['广式火锅', '老北京涮羊肉火锅', '牛肉火锅', '羊血火锅', '羊蝎子火锅', '烤鸭', '自助烧烤', '羊肉', '猪肚鸡', '面', '寿司', '寿喜锅', '日餐', '自助餐',
		 '汤包',
		 '锅贴', '串串火锅', '湘菜', '川菜', '东北铁锅炖', '早茶', '椰子鸡', '淮扬菜', '越南菜', '米线', '臊子面', '牛排', '西餐', '披萨', '炸鸡', '汉堡',
		 '肉蟹煲', '麻食', '烤肉', '菠菜面', '泡馍', '日式拉面', '螺蛳粉', '牛肉拉面', '延安沾沾', '葫芦鸡', '麻辣烫', '黄焖鸡', '钵钵鸡', '小龙虾', '新疆炒米粉',
		 '鱼火锅', '酸菜鱼', '烤鱼', '云南菜', '俄罗斯菜', '烤牛肉', '焖锅', '烤生蚝', '鲁菜', '泰国菜', '韩式部队锅', '手抓羊肉'
	, '徽菜牛蛙', '重庆纸包鱼', '陕菜']
menu3 = random.choice(menus)
print("请珍惜每一次的随机选择！！----", menu3)
Blanklines()

print("执行人在以下随机选取的菜品种选择一种菜品作为聚餐目标，请讨论作出决定！！！\n",menu1,menu2,menu3)
Blanklines()
input("请按回车键以关闭窗口，我们下次聚餐再见。")
