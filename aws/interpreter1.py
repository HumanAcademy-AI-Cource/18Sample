#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ライブラリのインポート
import boto3
import subprocess
import wave

################################
# ここから翻訳
################################

# 翻訳したい文章
input_text = "私はロボットです。"

# 確認のために表示
print("----------------------------------------------------")
print("○  翻訳する文章: 「{}」".format(input_text))
print("----------------------------------------------------")

# AWSを使った翻訳の準備
translate = boto3.client(service_name="translate")
# 文章を翻訳
translate_data = translate.translate_text(
    Text=input_text,
    SourceLanguageCode="ja",
    TargetLanguageCode="en"
)["TranslatedText"].encode("UTF-8")

# 確認のために表示
print("○  翻訳した文章: 「{}」".format(translate_data))
print("----------------------------------------------------")

################################
# ここから音声合成
################################

# 確認のために表示
print("○  発話させる文章: 「{}」".format(translate_data))
print("----------------------------------------------------")

# AWSを使った音声合成の準備
polly = boto3.client(service_name="polly")

# 音声合成を実行
speech_data = polly.synthesize_speech(
    Text=translate_data,
    OutputFormat='pcm',
    VoiceId='Salli'
)['AudioStream']

# 音声合成の結果をWAVデータとして保存する
filename = "speech.wav"
print("○  音声データを「{}」として保存".format(filename))
print("----------------------------------------------------")
wave_data = wave.open(filename, 'wb')
wave_data.setnchannels(1)
wave_data.setsampwidth(2)
wave_data.setframerate(16000)
wave_data.writeframes(speech_data.read())
# ファイルを閉じる
wave_data.close()

# 確認のために表示
print("○  保存した音声を再生")
print("----------------------------------------------------")
# 保存したWAVデータを再生
subprocess.check_call('aplay -D plughw:0 {}'.format("speech.wav"), shell=True)
print("プログラムを終了します")
