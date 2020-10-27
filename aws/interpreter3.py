#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ライブラリのインポート
import library # 自作のライブラリ

# 翻訳したい文章
input_text = "私はロボットです。"
# 翻訳を実行
translate_data = library.honyaku(input_text, "ja", "en")

# 確認のために表示
print("----------------------------------------------------")
print("○  翻訳した文章: 「{}」".format(translate_data))
print("----------------------------------------------------")

# 翻訳結果を使って音声合成
speech_data = library.onsei_gousei(translate_data)
# 音声データを保存
library.onsei_hozon(speech_data, "speech.wav")
# 音声データを再生
library.onsei_saisei("speech.wav")
