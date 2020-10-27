#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 自作の四則演算ライブラリを読み込む
import keisan

# 1 + 1は？
kekka1 = keisan.tashizan(1, 1)
print(kekka1)

# 30 + 40は？
kekka2 = keisan.tashizan(30, 40)
print(kekka2)

# 10 - 10は？
kekka3 = keisan.hikizan(10, 10)
print(kekka2)

# 10 × 10は？
kekka4 = keisan.kakezan(10, 10)
print(kekka3)

# 10 ÷ 10は？
kekka5 = keisan.warizan(10, 10)
print(kekka4)
