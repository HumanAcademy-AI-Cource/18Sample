#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ライブラリのインポート
import boto3
import subprocess
import wave

#####################################################
 # AWSを使った翻訳の関数
def honyaku(text, source, target):
    translate = boto3.client(service_name="translate")
    return translate.translate_text(
        Text=text,
        SourceLanguageCode=source,
        TargetLanguageCode=target
    )["TranslatedText"].encode("UTF-8")

# AWSを使った音声合成の関数
def onsei_gousei(text):
    polly = boto3.client(service_name="polly")
    return polly.synthesize_speech(
        Text=text,
        OutputFormat='pcm',
        VoiceId='Salli'
    )['AudioStream']

# 音声データを保存する関数
def onsei_hozon(data, filename):
    wave_data = wave.open(filename, 'wb')
    wave_data.setnchannels(1)
    wave_data.setsampwidth(2)
    wave_data.setframerate(16000)
    wave_data.writeframes(data.read())
    # ファイルを閉じる
    wave_data.close()

# 音声データを再生する関数
def onsei_saisei(filename):
    subprocess.check_call('aplay -D plughw:0 {}'.format(filename), shell=True)
#####################################################

# 翻訳したい文章
input_text = "私はロボットです。"
# 翻訳を実行
translate_data = honyaku(input_text, "ja", "en")

# 確認のために表示
print("----------------------------------------------------")
print("○  翻訳した文章: 「{}」".format(translate_data))
print("----------------------------------------------------")

# 翻訳結果を使って音声合成
speech_data = onsei_gousei(translate_data)
# 音声データを保存
onsei_hozon(speech_data, "speech.wav")
# 音声データを再生
onsei_saisei("speech.wav")
