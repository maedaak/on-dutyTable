#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
当番表をランダムで生成する簡単なPythonスクリプト
より公平にするには、生成後に微修正が必要
極力3連続の当番を避ける制約あり
"""

import random
import numpy as np

# Parameter Setting

# メンバーの氏名をリストで指定
members = ['A氏', 'B氏', 'C氏', 'D氏', 'E氏', 'F氏', 'G氏']

# 生成日数を指定
generateDays = 20

# 1回の当番の人数を指定
number = 3

# 極力3連続の当番をどの程度避けるべく試みるかの回数
# 数値が大きいほど動作が遅くなる
maxRetry = 1000

# 結果データで当番になったことを示すマーク
mark = "○"

members_len = len(members)
members_code = [i for i in range(members_len)]

schedule = np.zeros((members_len, generateDays))

for day in range(generateDays):
	# 3連続は極力避ける
    for i in range(maxRetry):
        flag = 0
        onDuty = random.sample(members_code, number)
        for j in onDuty:
            if day > 2 \
              and schedule[j][day-1] == 1 \
              and schedule[j][day-2] == 1:
    	        flag = 1
        if flag == 0:
    	    break
    for j in onDuty:
        schedule[j][day] = 1

print("", end="\t")
print("\t".join(members))
for day in range(generateDays):
	print(day, end="\t")
	for i in range(members_len):
	    if schedule[i][day-1] == 1:
	         print(mark, end="\t")
	    else:
	         print("-", end="\t")
	print()
print()