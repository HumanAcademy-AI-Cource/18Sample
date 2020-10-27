#!/usr/bin/env python
# -*- coding: utf-8 -*-

def tashizan(a, b):
    '''
    説明: 足し算をする関数
    入力: 数字a, 数字b
    出力: 計算結果(a + b)
    '''
    # 計算結果をkekkaという変数に入れる
    kekka = a + b
    # 計算結果が入ったkekkaを出力する
    return kekka

################################
# 作った関数を使って実際に足し算をしてみる

# 1+1は？
kekka1 = tashizan(1, 1)
print(kekka1)

# 30+40は？
kekka2 = tashizan(30, 40)
print(kekka2)
