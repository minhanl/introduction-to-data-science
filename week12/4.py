# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10Zf9FALuFGoo31qbOvUDqhRIEi_petyq
"""

# random 產生 1 個隨機數
import random

random.randint(1, 1000)
# random 產生 100 個隨機數
random_integers = [] # 隨機數
for i in range(100): # 產生個數
  rand_int = random.randint(1, 1000) # 範圍
  random_integers.append(rand_int)
print(random_integers)
print(len(random_integers))
# 找出第一大與第一小的數字
print(max(random_integers))
print(min(random_integers))
# 找出第二大與第二小的數字
rand_int_unique = set(random_integers)
rand_int_unique_list = list(rand_int_unique)
print(rand_int_unique_list)
rand_int_unique_list.sort()
print(rand_int_unique_list[1]) # second min
print(rand_int_unique_list[-2]) # second max