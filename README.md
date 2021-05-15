このプログラムはヒューマンアカデミー株式会社のAI入門講座で使用するプログラムです。

# 18Sample

### ディレクトリ構成
* aws
    * interpreter1.py
        * プログラム内に書かれている文書を翻訳して音声合成
    * interpreter2.py
        * プログラム内に書かれている文書を翻訳して音声合成（各処理の関数を作って利用したバージョン）
    * interpreter3.py
        * プログラム内に書かれている文書を翻訳して音声合成（interpreter2.pyで作った関数をライブラリして利用したバージョン）
    * library.py
        * 各処理の関数をまとめたライブラリファイル
* practice
    * practice1.py
        * 足し算を行うプログラム
    * practice2.py
        * 足し算を行うプログラム（足し算を行う関数を作って利用したバージョン）
    * practice3.py
        * 足し算+αを行うプログラム（practice2.pyで作った関数+αをライブラリして利用したバージョン）
    * keisan.py
        * 四則演算の関数をまとめたライブラリファイル
* translate_command_list/
    * translate_command_list.py
        * コマンドリストのコメントを日本語から英語に翻訳
    * command_lists
        * 日本語で書かれたコマンドリストを入れておくディレクトリ
    * en_command_lists
        * 英語に翻訳されたコマンドリストが出力されるディレクトリ（translate_command_list.pyを実行すると作成されます）
